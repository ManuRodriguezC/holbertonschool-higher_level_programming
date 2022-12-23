#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, date) {
  if (error) {
    console.log(error);
  } else {
    const objDate = JSON.parse(date);
    const dates = {};
    for (let pos = 1; pos <= 10; pos++) {
      let count = 0;
      for (let x = 0; x < objDate.length; x++) {
        if (objDate[x].completed === true && objDate[x].userId === pos) {
          count += 1;
        }
      }
      if (count != 0) {
        dates[pos] = count;
      }
    }
    console.log(dates);
  }
});
