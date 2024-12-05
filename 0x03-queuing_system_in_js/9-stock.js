import kue from "kue";
import express from "express";

const queue = kue.createQueue();

const listProducts = [
  {
    itemId: 1,
    itemName: "Suitcase 250",
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: "Suitcase 450",
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: "Suitcase 650",
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: "Suitcase 1050",
    price: 550,
    initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  return listProducts.find((item) => item.itemId === id) || null;
}

const redis = require("redis");
const { promisify } = require("util");

// Connect to Redis
const redisClient = redis.createClient();
redisClient.on("connect", () =>
  console.log("Redis client connected to the server")
);
redisClient.on("error", (err) =>
  console.error("Redis client not connected to the server:", err)
);

// Promisify Redis methods
const setAsync = promisify(redisClient.set).bind(redisClient);
const getAsync = promisify(redisClient.get).bind(redisClient);

// Reserve stock by item ID
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

// Get current reserved stock by item ID
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : null;
}

const express = require("express");
const app = express();
const PORT = 1245;

// List all products
app.get("/list_products", (req, res) => {
  res.json(listProducts);
});

// Get details of a specific product
app.get("/list_products/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: "Product not found" });
  }

  const currentQuantity =
    product.initialAvailableQuantity -
    ((await getCurrentReservedStockById(itemId)) || 0);

  res.json({
    ...product,
    currentQuantity,
  });
});

// Reserve a product
app.get("/reserve_product/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: "Product not found" });
  }

  const reservedStock = (await getCurrentReservedStockById(itemId)) || 0;
  const availableStock = product.initialAvailableQuantity - reservedStock;

  if (availableStock <= 0) {
    return res.json({ status: "Not enough stock available", itemId });
  }

  await reserveStockById(itemId, reservedStock + 1);
  res.json({ status: "Reservation confirmed", itemId });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
