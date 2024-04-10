solve = (num) => console.log(`Odd sum = ${num.toString().split('').map(x=>Number.parseInt(x))
.reduce((sum, num) => sum += num%2==1?num:0, 0)}, Even sum = ${num.toString().split('')
.map(x=>Number.parseInt(x)).reduce((sum, num) => sum += num%2==0?num:0, 0)}`)

solve(1000435);
solve(3495892137259234);