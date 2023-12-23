#!/usr/bin/node

exports.esrever = function (list) {
  const size = list.length;
  const len = Math.floor(list.length / 2);

  for (let i = 0; i < len; i++) {
    const temp = list[i];
    list[i] = list[size - 1 - i];
    list[size - 1 - i] = temp;
  }

  return list;
};
