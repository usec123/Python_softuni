function focused() {
    Array.from(document.querySelectorAll('body>div>div>input')).forEach(x => {
        x.addEventListener('focus', ()=>x.parentElement.classList.add('focused'));
        x.addEventListener('blur', ()=>x.parentElement.classList.remove('focused'))
    })
}