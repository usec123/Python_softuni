function solve(words, text) {
    words.split(', ').forEach(element => {
        text = text.replace(new RegExp(`(\\s)([*]{${element.length}})(\\s|$)`, 'g'), `$1${element}$3`)
    });
    console.log(text.trim());
}

solve('great','softuni is ***** place for learning new programming languages')