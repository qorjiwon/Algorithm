function solution(nums) {
    var answer = 0;
    for (let i = 0; i < nums.length; i++){
        for (let j = i+1; j < nums.length; j++){
            for (let k = j+1; k < nums.length; k++){
                let sum = nums[i]+nums[j]+nums[k]; 
                let ox = true;
                for (let t = 2; t < sum; t++){
                   if (sum%t === 0){
                       ox = false;
                       break;
                   } 
                }
                if (ox) answer += 1;
            }
        }
    }
    
    return answer;
}