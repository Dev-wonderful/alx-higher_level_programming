#!/usr/bin/node
exports.esrever = function (list) {
  const result = [];
  for (let i = list.length; i > 0; i--) {
    result.push(list[i - 1]);
  }
  return result;
};
