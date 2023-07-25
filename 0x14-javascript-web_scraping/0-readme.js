#!/usr/bin/node
// const request = require('request');
const fs = require('fs');
const { argv } = require('process');

const file = argv[2];
try {
  const data = fs.readFileSync(file, 'utf-8');
  console.log(data);
} catch (err) {
  console.error(err);
}
