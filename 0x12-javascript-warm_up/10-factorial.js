#!/usr/bin/node
function Factorialize (num) {
  if ((Number.isNaN(num)) || (num === 1)) {
    return 1;
  }
  return Factorialize(num - 1) * num;
}
console.log(Factorialize(parseInt(process.argv[2])));
