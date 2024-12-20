import kue from "kue";

const blacklistedNumbers = [4153518780, 4153518781];

const queue = kue.createQueue();

const sendNotification = (phoneNumber, message, job, done) => {
  // Tack the progress to 0%
  job.progress(0, 100);

  // Cheick if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track job progress to 50%
  job.progress(50, 100);
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );

  // Mark the job as done
  done();
};

queue.process("push_notification_code_2", 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  // call the sendNotificaion function
  sendNotification(phoneNumber, message, job, done);
});
