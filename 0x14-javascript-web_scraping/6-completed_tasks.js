#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, function (err, response, body) {
  if (err) {
    return;
  }
  const tasks = JSON.parse(body);
  tasks.forEach(task => {
    if (task.completed) {
      if (dict[task.userId]) {
        dict[task.userId]++;
      } else {
        dict[task.userId] = 1;
      }
    }
  });
  console.log(dict);
});
