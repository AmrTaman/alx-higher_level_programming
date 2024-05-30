#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    return;
  }
  fs.writeFile(fileName, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
