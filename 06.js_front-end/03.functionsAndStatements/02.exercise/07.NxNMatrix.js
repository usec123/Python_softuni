solve = (n) => console.log(((n.toString()+'_').repeat(n)+' ').repeat(n).trimEnd().split(' ').map(x => x.split('_').join(' ')).join('\n'))

solve(3)
solve(7)
solve(10)