#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let size = list.length - 1;

  for (; size >= 0; size--) {
    newList.push(list[size]);
  }
  return newList;
};
