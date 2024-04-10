solve = (arr) => arr.filter(x=>x!=='').sort((x, y) => x.localeCompare(y)).forEach((x,index) => console.log(`${index+1}.${x}`))

solve(["John", "Bob", "Christina", "Ema"]);