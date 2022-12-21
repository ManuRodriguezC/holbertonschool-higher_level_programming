#!/usr/bin/node
const process = require('process')
first = process.argv[2]

number = parseInt(first)
if (isNaN(number) === true) {
console.log('Not a number')
} else {
console.log('My number: ' + number)
}