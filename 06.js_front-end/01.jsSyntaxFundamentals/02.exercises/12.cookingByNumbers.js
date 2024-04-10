function solve(num, ...operations) {
    for (let op of operations){
        switch(op) {
            case 'chop':
                num /= 2;
                break;
            case 'dice':
                num = Math.sqrt(num);
                break;
            case 'spice':
                num += 1;
                break;
            case 'bake':
                num *= 3;
                break;
            case 'fillet':
                num -= 0.2*num;
                break;
        }
        console.log(num);
    }
}

solve('32', 'chop', 'chop', 'chop', 'chop', 'chop');
console.log('--------------------------------------');
solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet');
