#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

const url = argv[2];
request
  .get(url)
  .on('response', function (response) {
    console.log('code:', response.statusCode);
    // console.log(`code: ${response.statusCode}`);
  });
