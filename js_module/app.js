const greet = require('./great.js');
greet();
const greet1 = require('./greet2.js');
greet1.greet();
const greet2 = require('./greet3.js');
greet2.greet();
const greet3 = require('./greet4.js');
const grtr = new greet3();
grtr.greet();
