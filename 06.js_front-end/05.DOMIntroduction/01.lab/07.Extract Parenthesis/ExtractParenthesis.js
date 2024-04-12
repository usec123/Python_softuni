function extract(content) {
    return Array.from(document.getElementById(content).textContent.matchAll(/\(([\w -]+)\)/g))
    .map(x => x[1]).join('; ')
}