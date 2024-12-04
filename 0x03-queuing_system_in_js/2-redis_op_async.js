import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();

// Promisifing Redis commands
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

const setNewSchool = async (schoolName, value) => {
  const reply = await setAsync(schoolName, value);
  console.log("Reply:", reply);
};

const displaySchoolValue = async (schoolName) => {
  const value = await getAsync(schoolName);
  console.log(value);
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
