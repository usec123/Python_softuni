solve = (firstName, lastName, age) => Object.fromEntries([['firstName', firstName], ['lastName', lastName], ['age', age]])

console.log(solve('Peter', 'Pan', 20));