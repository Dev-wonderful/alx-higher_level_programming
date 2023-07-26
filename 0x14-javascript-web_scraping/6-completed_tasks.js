#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

function search (todos) {
  const completedTasks = {};
  todos.forEach((todo) => {
    if (todo.completed === true) {
      if (!(todo.userId in completedTasks)) {
        completedTasks[todo.userId] = 0;
        console.log('h');
      }
      completedTasks[todo.userId] += 1;
    }
  });
  return completedTasks;
}

const url = argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    console.log(search(todos));
  }
});
