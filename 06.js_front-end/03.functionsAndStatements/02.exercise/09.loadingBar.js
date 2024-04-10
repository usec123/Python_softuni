solve = (num) => console.log(`${num}% ${num===100?'Complete!\n':''}[${'%'.repeat(num/10)}${'.'.repeat(10-num/10)}]${num!==100?'\nStill loading...':''}`)

solve(30)
solve(50)
solve(100)