function addItem() {
    const textInputElement = document.getElementById('newItemText');
    const textValueElement = document.getElementById('newItemValue');
    const selectElement = document.getElementById('menu');

    const newElement = document.createElement('option');
    newElement.textContent = textInputElement.value;
    newElement.value = textValueElement.value;

    selectElement.appendChild(newElement);

    textInputElement.value = '';
    textValueElement.value = '';
}