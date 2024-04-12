function sumTable() {
    document.getElementById('sum').textContent = Array.from(document.querySelectorAll('tr>td:last-of-type')).map(x=>Number(x.textContent)).reduce((sum, num) => sum + num, 0)
}