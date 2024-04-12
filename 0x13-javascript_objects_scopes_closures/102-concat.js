#!/usr/bin/node
const files = require('files');
const i = files.readFileSync(process.argv[2], 'utf8');
const j = files.readFileSync(process.argv[3], 'utf8');
files.writeFileSync(process.argv[4], i + j);
