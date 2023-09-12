#!/usr/bin/node
const list = require('./100-data').list;
const arr = list.map((i, x) => i * x);
console.log(list);
console.log(arr);
