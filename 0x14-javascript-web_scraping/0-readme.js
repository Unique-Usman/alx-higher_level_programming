#!/usr/bin/node
// read and print the content
// of file

const fs = require('fs');
const process = require('process');
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
