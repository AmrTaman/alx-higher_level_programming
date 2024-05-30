#!/usr/bin/node
const request = require('request');
const number = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + number;
request(url, function (err, response, body) {
  if (err) {
    return;
  }
  console.log(JSON.parse(body).title);
});
