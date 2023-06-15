#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

const files = argv.slice(2);
const fileA = fs.readFileSync(files[0]).toString();
const fileB = fs.readFileSync(files[1]).toString();
fs.writeFileSync(files[2], `${fileA}${fileB}`);
