#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    const id = 'https://swapi-api.alx-tools.com/api/people/18/';
    let total = body.split('/people/18/').length - 1;

    console.log(total);
  }
});
