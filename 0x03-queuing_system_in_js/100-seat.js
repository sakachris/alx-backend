import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

// Create Express app
const app = express();
const PORT = 1245;

const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

const queue = kue.createQueue();

// Reserve seat function
const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const availableSeats = await getAsync('available_seats');
  return parseInt(availableSeats) || 0;
};

reserveSeat(50);

let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }
  
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });
  
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  
  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });
  
  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();
    if (currentSeats === 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }
    
    await reserveSeat(currentSeats - 1);
    if (currentSeats === 1) {
      reservationEnabled = false;
    }
    
    done();
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
