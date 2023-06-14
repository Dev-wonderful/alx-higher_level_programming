#!/usr/bin/node
const list = require('./100-data');

let i = 0;
let value;
const result = list.map((num) => {
  value = i * num;
  i++;
  return value;
});
console.log(list);
console.log(result);
