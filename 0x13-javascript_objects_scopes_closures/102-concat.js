#!/usr/bin/node

const fs = require('fs');

const data = fs.readFileSync(process.argv[2], 'utf8');
const data1 = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], data + data1, 'utf8');
