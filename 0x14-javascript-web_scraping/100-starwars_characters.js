#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(url, function (error, reponse, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    });
  }
});
