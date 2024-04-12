function extractText() {
    document.getElementById('result').textContent = Array.from(document.querySelectorAll('#items>*')).map(x => x.textContent).join('/n')
}