const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0].split('');
    len = str.length;
    str.forEach((value) => {
        if (value == value.toUpperCase()){
            rl.output.write(value.toLowerCase());
        }
        else {
            rl.output.write(value.toUpperCase());
        }
    });
});