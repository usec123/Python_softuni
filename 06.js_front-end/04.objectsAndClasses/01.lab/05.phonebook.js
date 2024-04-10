solve = (arr) => Object.entries(Object.fromEntries(arr.map(x => x.split(' ')))).forEach(x => console.log(`${x[0]} -> ${x[1]}`))

solve(['Tim 0834212554','Peter 0877547887','Bill 0896543112','Tim 0876566344'])
solve(['George 0552554','Peter 087587','George 0453112','Bill 0845344'])