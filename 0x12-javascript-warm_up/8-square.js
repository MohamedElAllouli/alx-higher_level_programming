#!/usr/bin/node
const s = process.argv[2];
if (isNaN(s)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < s; i++) {
    console.log('X'.repeat(s));
  }
}
