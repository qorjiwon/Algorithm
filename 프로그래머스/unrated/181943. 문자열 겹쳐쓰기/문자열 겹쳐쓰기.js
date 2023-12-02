function solution(my_string, overwrite_string, s) {
    var answer = my_string.split('');
    console.log(answer.join(''));
    console.log(overwrite_string.length);
    for(let i = 0; i < overwrite_string.length; i++){
        answer[s+i] = overwrite_string[i];
    }
    console.log(answer.join(''));
    return answer.join('');
}