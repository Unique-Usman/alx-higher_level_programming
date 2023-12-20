#!/usr/bin/node

if (!(+process.argv[2])) {
  console.log('Missing size');
} else if (parseInt(process.argv <= 0)) {
} else {
  const x = parseInt(process.argv[2]);
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      process.stdout.write('X');
    }
    if (i != x - 1) { process.stdout.write('\n'); }
  }
}
