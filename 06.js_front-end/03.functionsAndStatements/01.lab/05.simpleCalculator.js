solve = (a,b,operation) => console.log(eval(`${a} ${{'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}[operation]} ${b}`));

solve(5, 5, 'multiply')