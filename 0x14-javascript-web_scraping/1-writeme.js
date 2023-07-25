#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');

const file = argv[2];
const data = argv[3];
try {
  fs.writeFileSync(file, data, 'utf-8');
} catch (err) {
  console.log(err);
}
