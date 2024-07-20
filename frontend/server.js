const express = require('express');
const path = require('path');
const history = require('connect-history-api-fallback');

const app = express();

// Handle SPA history mode
app.use(history());

// Serve static files from the Vue app build directory
app.use(express.static(path.join(__dirname, 'dist')));

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});