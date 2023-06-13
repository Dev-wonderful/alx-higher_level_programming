#!/usr/bin/node
const { argv } = require('process');

const numbers = argv.slice(2);
let max = numbers[0];
let secondMax = 0;
if (numbers.length > 1) {
  for (let i = 0; i < numbers.length; i++) {
    secondMax = max;
    max = max > numbers[i] ? max : numbers[i];
  }
  console.log(secondMax);
} else {
  console.log(secondMax);
}
