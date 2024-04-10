solve = (str) => Object.entries(JSON.parse(str)).forEach(x => console.log(`${x[0]}: ${x[1]}`))

solve('{"name": "George", "age": 40, "town": "Sofia"}')