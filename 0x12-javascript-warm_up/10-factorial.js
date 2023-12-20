#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function fact (arg) {
  if (!arg || arg === 0 || arg === 1) {
    return 1;
  } else {
    return arg * fact(arg - 1);
  }
}

console.log(fact(arg));
