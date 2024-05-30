#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    return;
  }
  const data = JSON.parse(body).results;
  const len = data.filter(film =>
    film.characters.some(str => str.includes('/18/'))).length;
  console.log(len);
});
