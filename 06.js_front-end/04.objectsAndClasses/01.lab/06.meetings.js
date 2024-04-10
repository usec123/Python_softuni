function solve (arr) {
    meetings = {}
    arr.map(x => x.split(' ')).forEach(x => {
        if (meetings[x[0]]) console.log(`Conflict on ${x[0]}!`)
        else {
            console.log(`Scheduled for ${x[0]}`);
            meetings[x[0]] = x[1];
    }});
    Object.entries(meetings).forEach(x => console.log(`${x[0]} -> ${x[1]}`))
}

solve(['Monday Peter','Wednesday Bill', 'Monday Tim', 'Friday Tim']);
