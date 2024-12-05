import kue from "kue";

/**
 * Create push notification jobs and adds them to a queue
 * @param {Array} jobs - An array of job object containing phoneNumber and message
 * @param {Object} queue - The kue queue object.
 */

const createPushNotificationsJobs = (jobs, queue) => {
  // validate input: jobsmust be an array
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }

  jobs.forEach((jobData) => {
    const job = queue
      .create("push_notification_code_3", jobData) // Create a job in the que
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        } else {
          console.error(`Error creating job: ${err}`);
        }
      });

    job.on("complete", () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on("failed", (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    job.on("progress", (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
};
module.exports = createPushNotificationsJobs;
