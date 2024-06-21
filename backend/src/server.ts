import express, { Application, Request, Response } from 'express';
import mongoose from 'mongoose';
import bodyParser from 'body-parser';
import cors from 'cors';
import dotenv from 'dotenv';

dotenv.config();

const app: Application = express();
app.use(bodyParser.json());
app.use(cors());

const PORT = process.env.PORT || 5000;

app.get('/', (req: Request, res: Response) => {
    res.send('Festival Organizer API');
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

mongoose.connect(process.env.MONGODB_URI || '', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.log(err));