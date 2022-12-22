#!/usr/bin/node
const process = require('process');

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(first, second);
