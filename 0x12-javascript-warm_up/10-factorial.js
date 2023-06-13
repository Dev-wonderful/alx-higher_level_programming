#!/usr/bin/node
const { argv } = require('process');

function factorial (a) {
  if (a) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}

const result = factorial(parseInt(argv[2]));
console.log(result);
