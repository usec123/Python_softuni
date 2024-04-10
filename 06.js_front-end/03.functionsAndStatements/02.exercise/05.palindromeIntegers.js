solve = (nums) => nums.forEach(x => console.log(x.toString() === x.toString().split('').reverse().join('')))

solve([123,323,421,121])