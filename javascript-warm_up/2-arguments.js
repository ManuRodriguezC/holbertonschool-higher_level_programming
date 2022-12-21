#!/usr/bin/node
const process = require('process');

var args = process.argv
var count = args.length

if (count == 2) {
    console.log('No argument')
}

if (count == 3) {
    console.log('Argument found')
}

if (count == 4) {
    console.log('Arguments found')
}