#!/usr/bin/node
const fs = require('fs');
path = process.argv[2];
content = process.argv[3];
fs.writeFile(path, content, (err) => {
  if (err) {
    console.log(err);
  }
});
