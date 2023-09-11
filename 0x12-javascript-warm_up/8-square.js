#!/usr/bin/node
import { argv } from 'node:process';

if (argv[2] === undefined || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
