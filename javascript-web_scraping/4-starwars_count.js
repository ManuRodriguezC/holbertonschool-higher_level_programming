#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, 'utf-8', function (error, response, date) {
  if (error) {
    console.log(error);
  } else {
    const dateObj = JSON.parse(date).results;
    for (let x = 0; x < dateObj.length; x++) {
      for (let i = 0; i < dateObj[x].characters.length; i++) {
        const id = dateObj[x].characters[i].split('/')[5];
        if (id === '18') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
