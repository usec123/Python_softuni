function solve() {
    const selectMenuToElement = document.querySelector('#selectMenuTo');
    const binaryOptionElement = selectMenuToElement.querySelector('option');
    binaryOptionElement.value = 'binary';
    binaryOptionElement.textContent = 'Binary';
    const hexOptionElement = document.createElement('option');
    hexOptionElement.value = 'hexadecimal';
    hexOptionElement.textContent = 'Hexadecimal';
    selectMenuToElement.appendChild(hexOptionElement);

    document.querySelector('button').addEventListener('click', convert);

    function convert() {
        const number = Number(document.getElementById('input').value)
        const convertTo = {'binary' : 2, 'hexadecimal' : 16} [document.getElementById('selectMenuTo').value]

        document.getElementById('result').value = number.toString(convertTo).toUpperCase();
    }
}