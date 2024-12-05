import kue from "kue";

const queue = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};

// Process jobs in the 'push_notification_code' queue
queue.process("push_notification_code", (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function
  sendNotification(phoneNumber, message);

  // Mark the job as done
  done();
});
