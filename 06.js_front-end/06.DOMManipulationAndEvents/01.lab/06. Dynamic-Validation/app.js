function validate() {
    const pattern = /^[a-z]+@[a-z]+\.[a-z]+/g;
    const inputElement = document.getElementById('email');
    inputElement.addEventListener('change', ()=>{
        if (Array.from(inputElement.value.matchAll(pattern)).length === 0) inputElement.classList.add('error');
        else inputElement.classList.remove('error');
    });
}