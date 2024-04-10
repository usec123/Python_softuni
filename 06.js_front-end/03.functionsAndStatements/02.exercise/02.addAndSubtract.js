function solve(a,b,c){
    sum = (a,b) => a+b;
    subtract = (a,b,c) => console.log(sum(a,b)-c);
    subtract(a,b,c);
}

solve(23,6,10)