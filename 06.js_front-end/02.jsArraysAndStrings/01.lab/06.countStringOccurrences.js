solve = (text, word) => console.log(Array.from(text.matchAll(`\\b${word}\\b`)).length)

solve('This is a word and it also is a sentence','is')