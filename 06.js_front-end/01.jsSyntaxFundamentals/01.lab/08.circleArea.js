circleArea = (r) => {
    if (typeof r != 'number') {
        console.log(`We can not calculate the circle area, because we receive a ${typeof r}.`);
        return;
    }
    console.log((Math.PI*r**2).toFixed(2));
}

circleArea(5);
circleArea('name');
