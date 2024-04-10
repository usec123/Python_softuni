function solve(start, end){
    let nums = [];
    for (let i = start; i <= end; i++){
        nums.push(i);
    }
    console.log(nums.join(' '));
    console.log('Sum: ' + nums.reduce((sum, num) => sum+num));
}

solve(5, 10);
solve(0, 26);
solve(50, 60);
