function deleteByEmail() {
    const inputElement = document.getElementsByName('email')[0];
    const outputElement = document.getElementById('result');
    const tdElements = document.querySelectorAll('tbody tr td');

    console.log(tdElements);

    const toDelete = Array.from(tdElements).filter(x => x.textContent.includes(inputElement.value));
    outputElement.textContent = toDelete.length>0?'Deleted.':'Not found.';
    toDelete.forEach(x => x.parentElement.remove());
}