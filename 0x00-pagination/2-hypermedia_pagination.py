#!/usr/bin/env python3
"""Simple helper function"""


from typing import Tuple, List, Union, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    A function  that takes two integer arguments page and page_size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        data = self.dataset()

        start_index, end_index = index_range(page, page_size)

        return data[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[
            str, Union[int, None, list]
            ]:
        """Hypermedia pagination"""

        data = self.dataset()
        page_data = self.get_page(page, page_size)
        total_pages = (len(data) + page_size - 1) // page_size

        metadata = {
                'page_size': len(page_data),
                'page': page,
                'next_page': page + 1 if page < total_pages else None,
                'prev_page': page - 1 if page > 0 else None,
                'total_pages': total_pages
                }
        return metadata
