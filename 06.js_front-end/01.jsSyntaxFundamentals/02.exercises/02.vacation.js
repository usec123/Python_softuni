vacation = (qty, type, day) => {
    if (day=='Friday') day = 0;
    else if (day=='Saturday') day = 1;
    else day = 2;

    if (type == 'Students') type = 0;
    else if (type == 'Business') type = 1;
    else type = 2;

    prices = [[8.45, 9.80, 10.46], [10.90, 15.60, 16], [15, 20, 22.50]];
    price = prices[type][day];
    finalPrice = price*qty

    if (type == 0 && qty >= 30) finalPrice -= 0.15*finalPrice;
    if (type == 1 && qty >= 100) finalPrice = price*(qty-10);
    if (type == 2 && qty >= 10 && qty <= 20) finalPrice -= finalPrice*0.05;

    console.log(`Total price: ${finalPrice.toFixed(2)}`);
}

vacation(30,"Students","Sunday");
vacation(40,"Regular","Saturday");
