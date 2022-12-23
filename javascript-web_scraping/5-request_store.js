#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, 'utf-8', function (error, response, date) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(file, date, 'utf-8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
