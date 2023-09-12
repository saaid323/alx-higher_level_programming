#!/usr/bin/node
const PSquare = require('./5-square');
class Square extends PSquare {
  charPrint (c = 'X') {
    const line = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
}
module.exports = Square;
