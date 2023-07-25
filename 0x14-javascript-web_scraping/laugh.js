#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

function people (charactersArr) {
  const order = {};
  for (let i = 0; i < charactersArr.length; i++) {
    request(charactersArr[i], function (error, response, body) {
      if (error) {
        console.error(error);
      } else {
        const name = JSON.parse(body).name;
        order[i] = name;
        console.log(i);
      }
    });
    // console.log(i);
  }
  return order;
}

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    const order = people(characters);
    console.log(order);
    // for (let i = 0; i < order.keys().length; i++) {
    //   console.log(order[i]);
    // }
  }
});
