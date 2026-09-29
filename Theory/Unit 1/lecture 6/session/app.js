// app.js
const express = require('express');
const session = require('express-session');
const app = express();

// Middleware to handle sessions
app.use(session({
  secret: 'mySecretKey',       // used to sign session ID cookies
  resave: false,               // do not save if not modified
  saveUninitialized: true,     // save new sessions
  cookie: { maxAge: 60000 }    // cookie expiry: 1 minute
}));

// Set session variable
app.get('/login', (req, res) => {
  req.session.username = 'JohnDoe';
  res.send('Session started for ' + req.session.username);
});

// Access session data
app.get('/profile', (req, res) => {
  if (req.session.username) {
    res.send('Welcome ' + req.session.username);
  } else {
    res.send('Please log in first.');
  }
});

// Destroy session
app.get('/logout', (req, res) => {
  req.session.destroy(err => {
    if (err) return res.send('Error destroying session');
    res.send('Session destroyed successfully');
  });
});

app.listen(3000, () => console.log('Server running on port 3000'));
