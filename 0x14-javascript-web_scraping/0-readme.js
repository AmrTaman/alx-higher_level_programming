#!/usr/bin/node
const fs = require('fs');
const name = process.argv[2];

fs.readFile(name, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
