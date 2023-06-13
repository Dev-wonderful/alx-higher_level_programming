#!/usr/bin/node
const { argv } = require('process');

function add (a, b) {
  console.log(a + b);
}
const first = parseInt(argv[2]);
const second = parseInt(argv[3]);
add(first, second);
