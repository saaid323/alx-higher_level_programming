#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const films = JSON.parse(body);
    const character = films.characters;
    fetchCharacterNames(character);
  }
});

function fetchCharacterNames (characterUrls, index = 0) {
  if (index >= characterUrls.length) {
    return;
  }

  request.get(characterUrls[index], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name);
      fetchCharacterNames(characterUrls, index + 1);
    }
  });
}
