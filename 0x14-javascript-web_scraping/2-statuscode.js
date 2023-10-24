#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (eror, response, body) => {
  console.log(response.statusCode);
});
