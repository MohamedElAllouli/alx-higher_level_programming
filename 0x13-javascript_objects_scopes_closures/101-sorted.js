#!/usr/bin/node
const diction = require('./101-data.js').diction;
let newDict = {};
for (let k in diction) {
  if (newDict[diction[k]] === undefined) {
    newDict[diction[k]] = [k];
  } else {
    newDict[diction[k]].push(k);
  }
}
console.log(newDict);
