function solve(arr) {
    list = []
    arr.forEach(x => {
        list.push({
            'Name':x,
            'Personal Number': x.length
        })
    })
    list.forEach(x => {
        console.log(`Name: ${x['Name']} -- Personal Number: ${x['Personal Number']}`);
    })
}

solve(['Silas Butler','Adnaan Buckley','Juan Peterson','Brendan Villarreal'])