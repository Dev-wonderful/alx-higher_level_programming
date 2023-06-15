#!/usr/bin/node
const { dict } = require('./101-data');

const sortedObj = {};
let value;
for (const key in dict) {
  value = dict[key];
  if (sortedObj[value] === undefined) {
    sortedObj[value] = [];
    sortedObj[value].push(key);
  } else {
    sortedObj[value].push(key);
  }
}
console.log(sortedObj);
