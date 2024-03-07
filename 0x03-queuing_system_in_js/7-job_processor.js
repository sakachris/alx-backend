import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100); // Track progress

  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    console.error(errorMessage);
    done(new Error(errorMessage));
    return;
  }

  // Simulate processing delay
  setTimeout(() => {
    job.progress(50, 100); // Update progress
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }, 1000);
};

const queue = kue.createQueue({
  concurrency: 2 // Process two jobs at a time
});

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

console.log('Job processor is running...');
