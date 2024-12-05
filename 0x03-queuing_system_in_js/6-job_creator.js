//import redis from "redis";
import kue from "kue";

const queue = kue.createQueue();

// Create a job
const jobData = {
  phoneNumber: "00223 94 16 29 03",
  message: "A test message",
};

const job = queue.create("push_notification_code", jobData).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

// Event listener for the job
job.on("complete", () => {
  console.log("Notification job completed");
});

job.on("failed", () => {
  console.log("Notification job failed");
});
