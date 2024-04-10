solve = (text) => Array.from(text.matchAll(/#([a-zA-Z]+)/g)).forEach(x => console.log(x[1]))

solve('Nowadays everyone uses # to tag a #special word in #socialMedia')
solve('The symbol # is known #variously in English-speaking #regions as the #number sign')