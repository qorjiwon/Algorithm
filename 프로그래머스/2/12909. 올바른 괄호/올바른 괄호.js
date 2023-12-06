function solution(s){
    var x = 0;
    for (let i = 0; i < s.length; i++){
        if (s[i] === '('){
            x++;
        } else {
            x--;
        }
        if (x<0){
            return false;
        }
    }
    return x==0;
}