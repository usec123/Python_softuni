promotions = (day, age) => {
    day = (day == 'Weekday') ? 0 : (day == 'Weekend') ? 1 : 2;
    age = (age < 0 || age > 122) ? null : (age<=18) ? 0 : (age<=64) ? 1 : 2
    if (age == null){
        console.log('Error!');
        return;
    }
    prices = [[12,18,12],[15,20,15],[5,12,10]];
    console.log(`${prices[day][age]}$`)
}

promotions('Weekday', 42);
promotions('Holiday', -12);
promotions('Holiday', 15);
