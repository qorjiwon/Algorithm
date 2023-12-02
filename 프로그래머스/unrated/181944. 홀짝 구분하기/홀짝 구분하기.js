const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    let result = Number(input)%2==0 ? "is even" : "is odd";
    console.log(Number(input), result);
});