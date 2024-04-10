function solve(a, operator, b) {
    eval(`console.log((${a} ${operator} ${b}).toFixed(2))`);
}

solve(5, '+', 10);
solve(25.5, '-', 3);