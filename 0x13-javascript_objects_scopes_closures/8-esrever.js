#!/usr/bin/node
exports.esrever = function (list) {
  const new_list = [];
  for (let x = list.length - 1; x >= 0; x--) {
    new_list.push(list[x]);
  }
  return new_list;
}
