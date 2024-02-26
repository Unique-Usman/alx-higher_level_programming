#!/usr/bin/node
// Write a script that gets the contents
// of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const process = require('process');

request.get(`${process.argv[2]}/`,
  function (err, response, body) {
    if (err) {
      console.log(err);
      return;
    }
    fs.writeFile(process.argv[3], body, err => {
      if (err) {
        console.log(err);
        return err;
      }
    });
  }
);
