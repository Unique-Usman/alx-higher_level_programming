#!/usr/bin/node
// Display the status code of a
// get request

const request = require('request');
const process = require('process');

request.get(process.argv[2]).on(
  'response', function (response) {
    console.log(`code: ${response.statusCode}`);
  }
);
