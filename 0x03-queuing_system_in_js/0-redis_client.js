import redis from "redis";
const client = redis.createClient();

client.on("connect", (err) => {
  if (!err) {
    console.log("Redis client connected to the server");
  } else {
    console.log(`Redis client not connected to the server: ${err}`);
  }
});
