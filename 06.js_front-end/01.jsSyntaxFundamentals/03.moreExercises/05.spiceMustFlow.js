function solve(yield) {
    let extracted = 0;
    const workersConsumption = 26;
    days = 0;

    while (yield >= 100){
        extracted += yield;
        yield -= 10;
        extracted -= workersConsumption < extracted ? workersConsumption : extracted;
        days++;
    }
    extracted -= workersConsumption < extracted ? workersConsumption : extracted;
    console.log(days);
    console.log(extracted);
}

solve(111);
solve(450);