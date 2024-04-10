largestNum = (a,b,c) => {
    console.log(`The largest number is ${[a,b,c].sort().reverse()[0]}.`)
    console.log([a,b,c].sort())
}

largestNum(-1,8,16)