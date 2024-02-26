#!/usr/bin/node
// Compute the number of task
// computed by user id

const request = require('request');
const process = require('process');

request.get(`${process.argv[2]}`,
  function (err, _, body) {
    if (err) {
      console.log(err);
      return;
    }
    const ans = {};

    const data = JSON.parse(body);
    for (const datum of data) {
      if (datum.completed === true) {
        if (datum.userId in ans) {
          ans[datum.userId]++;
        } else {
          ans[datum.userId] = 1;
        }
      }
    }

    console.log(ans);
  });
