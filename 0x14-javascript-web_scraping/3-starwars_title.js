#!/usr/bin/node
// Print the title of a star wars
// movie where the episode number
// matches a given integer

const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`,
  function (err, response, body) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(JSON.parse(body).title);
  }
);
