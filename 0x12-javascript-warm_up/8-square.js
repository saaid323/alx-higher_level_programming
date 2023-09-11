#!/usr/bin/node
import { argv } from 'node:process';

const x = parseInt(process.argv[2]);
if (argv[2] === undefined || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
