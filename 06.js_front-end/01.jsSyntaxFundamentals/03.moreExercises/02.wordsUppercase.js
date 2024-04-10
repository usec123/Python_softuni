function solve(text) {
    console.log(text.replace(/[^\w]+/g, ' ').toUpperCase().split(' ').filter(x => x!=='').join(', '));
}

solve('Hi, how are you?');
solve('hello');
