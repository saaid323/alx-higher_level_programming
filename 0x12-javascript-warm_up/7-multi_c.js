#!/usr/bin/node
import { argv } from 'node:process';

let i = 0;
if (argv[2] === undefined || isNaN(argv[2])) {
	console.log('Missing number of occurrences');
}
while (i < argv[2]) {
  console.log('C is fun');
  i++;
}
