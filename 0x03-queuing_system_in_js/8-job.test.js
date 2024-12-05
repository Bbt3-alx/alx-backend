const chai = require("chai");
const expect = chai.expect;
const kue = require("kue");
const createPushNotificationsJobs = require("./8-job");

// Create a Kue queue
const queue = kue.createQueue();

describe("createPushNotificationsJobs", () => {
  // Before running tests, enable test mode to avoid processing jobs
  before(() => {
    queue.testMode.enter();
  });

  // After all tests, clear the queue and exit test mode
  after(() => {
    queue.testMode.clear(); // Clear any jobs in the queue
    queue.testMode.exit(); // Exit test mode
  });

  // Clear the queue before each test
  beforeEach(() => {
    queue.testMode.clear();
  });

  it("should throw an error if jobs is not an array", () => {
    const invalidInput = "not an array";

    expect(() => createPushNotificationsJobs(invalidInput, queue)).to.throw(
      "Jobs is not an array"
    );
  });

  it("should create jobs for each object in the jobs array", () => {
    const jobs = [
      { phoneNumber: "1234567890", message: "This is a test message 1" },
      { phoneNumber: "0987654321", message: "This is a test message 2" },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(jobs.length);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });

  it("should log job creation for each job", () => {
    const jobs = [
      { phoneNumber: "1234567890", message: "This is a test message 1" },
      { phoneNumber: "0987654321", message: "This is a test message 2" },
    ];

    // Spy on console.log
    const logSpy = chai.spy.on(console, "log");

    createPushNotificationsJobs(jobs, queue);

    expect(logSpy).to.have.been.called.with(
      `Notification job created: ${queue.testMode.jobs[0].id}`
    );
    expect(logSpy).to.have.been.called.with(
      `Notification job created: ${queue.testMode.jobs[1].id}`
    );

    // Restore console.log
    chai.spy.restore(console);
  });
});
