#!/usr/bin/node
const { argv } = require('process');
const value = isNaN(parseInt(argv?.[2])) ? 'Not a number' : `My number: ${parseInt(argv[2])}`;
console.log(value);
