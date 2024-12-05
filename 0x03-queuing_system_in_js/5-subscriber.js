import redis from "redis";

const client = redis.createClient();

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the channel
client.subscribe("holberton school channel");

// Handle message
client.on("message", (chanel, message) => {
  console.log(`Recived message: ${message}`);

  // If the message is 'KILL_SERVER', unsubscribe and quit
  if (message === "KILL_SERVER") {
    client.unsubscribe();
    client.quit();
  }
});
