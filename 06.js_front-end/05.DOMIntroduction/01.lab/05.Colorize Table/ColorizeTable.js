function colorize() {
    Array.from(document.querySelectorAll('tr:nth-child(2n)')).forEach(x => x.style.background='Teal')
}