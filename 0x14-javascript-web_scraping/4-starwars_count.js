#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    return;
  }
  const data = JSON.parse(body).results;
  const len = data.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')).length;
  console.log(len);
});
