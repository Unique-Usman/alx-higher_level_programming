#!/usr/bin/node
// write content to a file
// file:= process 2
// content:= process 3
const fs = require('fs');
const process = require('process');

fs.writeFile(process.argv[2], process.argv[3], err => {
  if (err) {
    console.log(err);
    return err;
  }
});
