#!/usr/bin/node

// Import the dictionary of occurrences by user ID from 101-data.js
const { dict } = require('./101-data');

// Create an empty dictionary for the new result
const newDict = {};
for (const key in dict) {
  const value = dict[key];
  if (!newDict[value]) {
    newDict[value] = [];
  }
  newDict[value].push(parseInt(key));
}
console.log(newDict);
