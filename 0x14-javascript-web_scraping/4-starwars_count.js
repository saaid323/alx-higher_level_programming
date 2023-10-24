#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    const id = 'https://swapi-api.alx-tools.com/api/people/18/';
    let total = 0;

    for (let i = 0; i < film.results.length; i++) {
      if (film.results[i].characters.includes(id)) {
        total++;
      }
    }

    console.log(total);
  }
});
