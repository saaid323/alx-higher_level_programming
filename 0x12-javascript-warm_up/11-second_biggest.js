#!/usr/bin/node

function findSecondLargest (args) {
  if (args.length <= 2) {
    return 0;
  }
  const integers = Array.from(new Set(args.map(arg => parseInt(arg))));
  integers.sort((a, b) => b - a);
  return integers[1];
}
const args = process.argv.slice(2);
const secondLargest = findSecondLargest(args);

console.log(secondLargest);
