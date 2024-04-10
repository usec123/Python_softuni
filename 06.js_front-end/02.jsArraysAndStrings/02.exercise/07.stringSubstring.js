solve = (word, text) => console.log(word + (([] + [text.match(new RegExp(`\\b(${word})\\b`, 'gi'))]).length === 0 ? ' not found!':''))

solve('javascript','JavaScript is the best programming language')

solve('python','JavaScript is the best programming language')
