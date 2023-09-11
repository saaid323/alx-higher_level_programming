#!/usr/bin/node
import { argv } from 'node:process';

if (argv.length === 0) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
