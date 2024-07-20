// Import necessary ES module features
import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

// Convert file URL to path for __dirname equivalent
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Initialize express app
const app = express();
const port = 3000;

// Serve static files from a directory named 'public'
app.use(express.static(path.join(__dirname, 'public')));

// Define a route
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});