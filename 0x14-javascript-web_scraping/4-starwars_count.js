#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = `${argv[2]}/18`;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log((data?.films)?.length);
  }
});
