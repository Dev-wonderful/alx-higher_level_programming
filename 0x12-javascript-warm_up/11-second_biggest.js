#!/usr/bin/node
const { argv } = require('process');

const numbers = argv.slice(2);
let secondMax = 0;
if (numbers.length > 1) {
  numbers.sort((a, b) => a - b);
  // console.log(numbers);
  secondMax = numbers[numbers.length - 2];
  console.log(secondMax);
} else {
  console.log(secondMax);
}
