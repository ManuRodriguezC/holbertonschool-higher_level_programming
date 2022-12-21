#!/usr/bin/node
const process = require('process');
const first = process.argv[2];

const number = parseInt(first);

if (isNaN(number) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
