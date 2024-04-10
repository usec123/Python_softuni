function solve(x1, y1, x2, y2) {
    console.log(`{${x1}, ${y1}} to {0, 0} is ${!Math.sqrt(x1**2 + y1**2).toString().includes('.') ? 'valid' : 'invalid'}`);
    console.log(`{${x2}, ${y2}} to {0, 0} is ${!Math.sqrt(x2**2 + y2**2).toString().includes('.') ? 'valid' : 'invalid'}`);
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${!Math.sqrt((x1-x2)**2 + (y1-y2)**2).toString().includes('.') ? 'valid' : 'invalid'}`);
}

solve(3, 0, 0, 4);
solve(2, 1, 1, 1);
