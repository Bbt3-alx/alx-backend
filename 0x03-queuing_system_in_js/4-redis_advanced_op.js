import redis from "redis";
//import { promisify } from "util";
const client = redis.createClient();

// const hsetAsync = promisify(client.hset).bind(client);
// const hgetallAsync = promisify(client.hgetall).bind(client);

const setHash = () => {
  const schools = {
    Portland: 50,
    Seattle: 80,
    "New York": 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const [field, value] of Object.entries(schools)) {
    client.hset("HolbertonSchools", field, value, redis.print);
  }
};

const displayHash = (key) => {
  client.hgetall(key, (err, reply) => {
    if (err) {
      console.error("Error:", err);
    } else {
      console.log(reply);
    }
  });
};

setHash();
displayHash("HolbertonSchools");
