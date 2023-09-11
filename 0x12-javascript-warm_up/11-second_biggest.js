#!/usr/bin/node
import { argv } from 'node:process';
if (argv.length <= 3) {
  console.log('0');
} else {
  const arr = argv.slice(2).map(Number);
  const second = arr.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
