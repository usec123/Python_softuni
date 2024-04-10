function solve(num) {
    num = num.toString();
    let lastDigit = num[0], sum = 0, isSame = true;
    for (var char of num) {
        if (char !== lastDigit) isSame = false;
        sum += +char;
    }
    console.log(isSame);
    console.log(sum);
}

solve(2222222);
solve(1234);
