#!/usr/bin/node
const process = require('process');
if (process.argv.length === 2) {
  console.log('Missing number of occurences')
}
if (process.argv.length === 3) {
  if (process.argv[2] > 0) {
    for (let x = 0; x < process.argv[2]; x++) {
      console.log('C is fun')
    }
}}
