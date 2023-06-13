#!/usr/bin/node
function addMeMaybe (x, theFunction) {
  x++;
  theFunction(x);
}

module.exports = { addMeMaybe };
