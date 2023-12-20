#!/usr/bin/node

if (!process.argv[2]) {
  console.log('No argument');
} else {
  const arr = process.argv.slice(2);
  arr.forEach(element => {
    console.log(element);
  });
}
