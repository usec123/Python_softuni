solve = (start, end) =>
    console.log(...Array.from(Array(end.codePointAt(0)>=start.codePointAt(0)?end.codePointAt(0)-start.codePointAt(0)-1:start.codePointAt(0)-end.codePointAt(0)-1).keys())
    .map(x => String.fromCharCode(1+((end.codePointAt(0)<=start.codePointAt(0)?end.codePointAt(0):start.codePointAt(0)) + x))))

solve('a','d');
solve('#', ':');