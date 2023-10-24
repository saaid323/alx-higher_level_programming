#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const films = JSON.parse(body);
    for (const person of films.characters) {
      request(person, (err, res, body) => {
        if (!err && res.statusCode === 200) {
          const pers = JSON.parse(body);
          console.log(pers.name);
        }
      });
    }
  }
});
