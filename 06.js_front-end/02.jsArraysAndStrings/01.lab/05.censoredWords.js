solve = (text, word='') => console.log(text.replace(new RegExp(`${word}`, 'gi'), '*'.repeat(word.length)))

solve('A small sentence with some words','small')