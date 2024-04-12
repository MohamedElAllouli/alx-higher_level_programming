#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDict = {};
for (let i in dict) {
  if (newDict[dict[i]] === undefined) {
    newDict[dict[i]] = [i];
  } else {
    newDict[dict[i]].push(i);
  }
}
console.log(newDict);
