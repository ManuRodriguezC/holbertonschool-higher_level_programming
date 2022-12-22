#!/usr/bin/node
const process = require('process')
const list = process.argv
const size = list.length
const listnum = []

for (let x = 2; x < size; x++) {
  listnum.push(parseInt(list[x]))
}

listnum.sort(function (a, b) {
  return (a - b);
});
console.log(listnum)
if (listnum.length === 0 || listnum.length === 1) {
    console.log(0);
  } else {
    console.log(listnum[listnum.length - 2]);
  }