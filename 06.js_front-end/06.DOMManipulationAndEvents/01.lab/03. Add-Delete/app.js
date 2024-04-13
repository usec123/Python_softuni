function addItem() {
    const inputElement = document.getElementById('newItemText');
    const ulElement = document.getElementById('items');

    const newElement = document.createElement('li');
    newElement.textContent = inputElement.value;

    const anchorElement = document.createElement('a');
    anchorElement.href = '#'
    anchorElement.textContent = '[Delete]';
    anchorElement.addEventListener('click', () => newElement.remove());
    newElement.appendChild(anchorElement);

    ulElement.appendChild(newElement);
    inputElement.value = '';
}