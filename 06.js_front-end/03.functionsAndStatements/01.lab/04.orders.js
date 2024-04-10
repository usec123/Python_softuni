solve = (product, qty) => console.log(eval(`(${{'coffee':1.5, 'water':1, 'coke':1.4, 'snacks':2}[product]}*${qty}).toFixed(2)`));

solve('water', 5)
solve('coffee', 2)