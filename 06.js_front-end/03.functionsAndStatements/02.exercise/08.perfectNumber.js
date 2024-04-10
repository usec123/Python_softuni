//solve = (n) => console.log([...Array(Math.floor(n/2)).keys()].slice(1).filter(x => n%(x+1)===0).reduce((sum, num) => sum += num + 1, 0)===n-1?'We have a perfect number!':'It\'s not so perfect.')

function solve(n) {
    let divisors = [1];
    for (let i = 2; i <= Math.floor(n/2); i++)
        if (n%i===0) divisors.push(i);
    console.log(divisors.reduce((sum, num) => sum += num, 0)===n?
        'We have a perfect number!':'It\'s not so perfect.')
}


solve(6)
