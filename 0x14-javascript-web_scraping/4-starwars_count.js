#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

function search (films) {
  let numOfFilms = 0;
  films.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes('18')) {
        numOfFilms++;
      }
    });
  });
  return numOfFilms;
}

const url = argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const results = JSON.parse(body).results;
    console.log(search(results));
  }
});
