function solve(num){
    num = num.toString();
    sum = 0;
    for (let char of num) {
        sum += +char;
    }
    console.log(sum);
}

solve(245678);
solve(97561);
solve(543);
