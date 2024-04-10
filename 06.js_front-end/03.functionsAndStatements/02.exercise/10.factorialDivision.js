function solve(a,b) {
    function fact(a) {
        if (a===1) return a;
        return a*fact(a-1);
    }

    console.log((fact(a)/fact(b)).toFixed(2));
}


solve(5,2)
solve(6,2)