#!/usr/bin/node
import { argv } from 'node:process';

let i = 0;
while (i < argv[2]) {
  console.log('C is fun');
  i++;
}
