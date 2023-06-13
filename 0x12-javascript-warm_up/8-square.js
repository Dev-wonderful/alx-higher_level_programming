#!/usr/bin/node
const { argv } = require('process');
let value = argv[2];
value = parseInt(value);
let square;
if (value) {
  for (let i = 0; i < value; i++) {
    square = '';
    for (let j = 0; j < value; j++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
