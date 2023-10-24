#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request.get(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completed = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        if (completed[userId]) {
          completed[userId]++;
        } else {
          completed[userId] = 1;
        }
      }
    });
    console.log(completed);
  }
});
