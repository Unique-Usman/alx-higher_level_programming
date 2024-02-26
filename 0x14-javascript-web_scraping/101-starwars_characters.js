#!/usr/bin/node
// Print all the characters of a
// Star war movie

const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`,
  function (err, response, body) {
    if (err) {
      console.log(err);
      return;
    }
    const data = JSON.parse(body);
    for (const char of data.characters) {
      request.get(`${char}`,
        function (err, response, body) {
          if (err) {
            console.log(err);
            return;
          }
          const data = JSON.parse(body);
          console.log(data.name);
        }
      );
    }
  }
);
