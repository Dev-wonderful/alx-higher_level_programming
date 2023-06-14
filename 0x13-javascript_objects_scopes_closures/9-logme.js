#!/usr/bin/node
exports.logMe = function (item) {
  let calls = 0;
  console.log(`${calls}: ${item}`);
  calls++;
};
