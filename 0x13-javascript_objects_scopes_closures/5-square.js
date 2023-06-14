#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (l) {
    super(l, l);
  }
}

module.exports = Square;
