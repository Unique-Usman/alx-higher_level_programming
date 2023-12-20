#!/usr/bin/node

let list = process.argv.slice(2);
list = list.map((x) => parseInt(x));

if (list.length <= 1) {
  console.log(0);
} else {
  list = list.sort((a, b) => b - a);
  console.log(list[1]);
}
