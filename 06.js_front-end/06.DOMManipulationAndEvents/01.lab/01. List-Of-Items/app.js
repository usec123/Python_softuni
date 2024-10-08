function addItem() {
    const itemsListElement = document.getElementById('items');
    const inputElement = document.getElementById('newItemText');

    const newElement = document.createElement('li');
    newElement.textContent = inputElement.value;
    itemsListElement.appendChild(newElement);
    inputElement.value = '';
}