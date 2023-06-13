#!/usr/bin/node
const { argv } = require('process');
const value = argv?.[2];
if (value) {
  console.log(value);
} else {
  console.log('No argument');
}
