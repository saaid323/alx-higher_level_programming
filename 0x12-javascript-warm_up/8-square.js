#!/usr/bin/node
import { argv } from 'node:process';

const x = parseInt(argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
