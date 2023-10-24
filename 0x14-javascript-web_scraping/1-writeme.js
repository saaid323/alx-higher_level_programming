#!/usr/bin/node
const fs = require('fs');
path = process.argv[2];
content = process.argv[3];
fs.write(path, content, (err) => {
	`
