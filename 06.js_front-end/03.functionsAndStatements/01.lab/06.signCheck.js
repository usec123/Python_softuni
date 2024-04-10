solve = (a,b,c) => console.log([a,b,c].map(x => x.toString()[0]==='-'?1:0).reduce((sum, num) => sum + num, 0)%2===0?'Positive':'Negative');

solve(5,12,-15)
solve(-6,-12,14)