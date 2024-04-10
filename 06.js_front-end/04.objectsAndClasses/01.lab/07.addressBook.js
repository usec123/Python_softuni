function solve (arr) {
    let addressBook = {}
    arr.map(x=>x.split(':')).forEach(x => addressBook[x[0]] = x[1])
    addressBook = Object.entries(addressBook).sort((x, y) => x[0].localeCompare(y[0]))
    for (let x of addressBook) console.log(`${x[0]} -> ${x[1]}`)
}

solve(['Tim:Doe Crossing','Bill:Nelson Place','Peter:Carlyle Ave','Bill:Ornery Rd'])
