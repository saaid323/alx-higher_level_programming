#!/usr/bin/node
import { argv } from 'node:process';

if (argv[2] === undefined) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
