#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/people/18';
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log((data?.films)?.length);
  }
});
