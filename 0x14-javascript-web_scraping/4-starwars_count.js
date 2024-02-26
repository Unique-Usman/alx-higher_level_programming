#!/usr/bin/node
// Print the number of movies
// where the characer "Wedges Antilles"
// is Present

const request = require('request');
let count = 0;

request.get(`${process.argv[2]}/`,
  function (err, response, body) {
    if (err) {
      console.log(err);
      return;
    }
    const data = JSON.parse(body);
    for (const datum of data.results) {
      for (const str of datum.characters) {
        if (str.includes('18')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
);
