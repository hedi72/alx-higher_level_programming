#!/usr/bin/node

let printTimes = parseInt(process.argv[2]);
if (isNaN(printTimes) || process.argv[2] === undefined) {
  console.log("Missing number of occurrences");
} else {
  for (let i = 0; i < printTimes; i++) {
    console.log("C is fun");
  }
}
