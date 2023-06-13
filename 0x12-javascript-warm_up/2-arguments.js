#!/usr/bin/node
const { argv } = require('process');
const argsNum = argv.length - 2;
if (argsNum > 1) {
  console.log('Arguments found');
} else if (argsNum > 0) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
