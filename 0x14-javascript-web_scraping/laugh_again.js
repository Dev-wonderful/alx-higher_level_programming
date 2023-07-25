#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

function people (charactersArr) {
  const order = [];
  let result;
  for (let i = 0; i < charactersArr.length; i++) {
    result = new Promise((resolve, reject) => {
      request(charactersArr[i], function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const name = JSON.parse(body).name;
          resolve(name);
          // order[i] = name;
          // console.log(i);
        }
      });
    });
    order.push(result.then((name) => console.log(name)));
    // console.log(i);
  }
  return Promise.all(order);
}

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    people(characters);
    // console.log(order)
    // for (let i = 0; i < order.keys().length; i++) {
    //   console.log(order[i]);
    // }
  }
});
