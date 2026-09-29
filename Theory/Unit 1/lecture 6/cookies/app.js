const express = require('express');
const cookieParser = require('cookie-parser');
const app = express();

app.use(cookieParser());

// Set a cookie
app.get('/setcookie', (req, res) => {
  res.cookie('username', 'JohnDoe', {
    maxAge: 3600000, // 1 hour
    httpOnly: true,  // not accessible by JavaScript
    secure: false     // true only if using HTTPS
  });
  res.send('Cookie has been set!');
});

// Read a cookie
app.get('/getcookie', (req, res) => {
  const user = req.cookies.username;
  if (user) {
    res.send('Welcome back, ' + user);
  } else {
    res.send('No cookie found.');
  }
});

// Delete a cookie
app.get('/deletecookie', (req, res) => {
  res.clearCookie('username');
  res.send('Cookie deleted.');
});

app.listen(3000, () => console.log('Server running on port 3000'));
