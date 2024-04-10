function solve(speed, road){
    speedLimits = {'motorway': 130, 'interstate': 90, 'city': 50, 'residential': 20}

    console.log(speed <= speedLimits[road] ? `Driving ${speed} km/h in a ${speedLimits[road]} zone` : 
    `The speed is ${speed - speedLimits[road]} km/h faster than the allowed speed of ${speedLimits[road]} - ${
        speed-speedLimits[road]<=20 ? 'speeding' : speed-speedLimits[road] <= 40 ? 'excessive speeding' : 'reckless driving'
    }`);
}

solve(40, 'city');
solve(21, 'residential');
solve(120, 'interstate');
solve(200, 'motorway');
