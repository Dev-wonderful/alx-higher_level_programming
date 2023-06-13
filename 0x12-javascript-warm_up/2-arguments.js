#!/usr/bin/node
const { argv } = require('node:process');
const argsNum = argv.length - 2;
if (argsNum > 0) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
