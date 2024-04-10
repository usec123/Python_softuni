solve = (text='') => console.log(Array.from(text.matchAll(/[A-Z][a-z]*/g)).join(', '))

// solve('SplitMeIfYouCanHaHaYouCantOrYouCan')
solve('fajoag')