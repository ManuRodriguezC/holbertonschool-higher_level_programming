#!/usr/bin/node
const process = require('process');
if (process.argv.length === 2) {
  console.log('Missing size');
} else {
  if (isNaN(process.argv[2]) === true) {
    console.log('Missing size');
  }
}
let squeare = '';
for (let width = 0; width < process.argv[2]; width++) {
  squeare += 'X';
}
for (let height = 0; height < process.argv[2]; height++) {
  console.log(squeare);
}
