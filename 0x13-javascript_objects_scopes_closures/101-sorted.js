#!/usr/bin/node

const obj = require('./101-data').dict;

const newObj = {};

for (const [k, v] of Object.entries(obj)) {
  if (!newObj[`${v}`]) {
    newObj[`${v}`] = [];
  }
  newObj[`${v}`].push(k);
}

console.log(newObj);
