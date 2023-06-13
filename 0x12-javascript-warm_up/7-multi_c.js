#!/usr/bin/node
const { argv } = require('process');
let value = argv[2];
value = parseInt(value);
let i = 0;
if (value) {
  while (i < value) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
