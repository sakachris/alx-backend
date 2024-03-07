import kue from 'kue';

const jobs = [
  { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153538781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153118782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4159518782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4158718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153818782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4154318781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4151218782', message: 'This is the code 4321 to verify your account' }
];

const queue = kue.createQueue();

const processJob = (job, done) => {
  const { phoneNumber, message } = job.data;
  // Simulating job processing time
  setTimeout(() => {
    console.log(`Notification job ${job.id} completed`);
    done();
  }, 2000);
};

queue.process('push_notification_code_2', (job, done) => {
  processJob(job, done);
});

// Loop through the array of jobs and create jobs for each object
jobs.forEach((jobData, index) => {
  queue.create('push_notification_code_2', jobData)
    .save((err) => {
      if (!err) {
        console.log(`Notification job created: ${jobData.phoneNumber} - ${jobData.message}`);
      } else {
        console.error(`Notification job ${index} failed: ${err}`);
      }
    });
});
