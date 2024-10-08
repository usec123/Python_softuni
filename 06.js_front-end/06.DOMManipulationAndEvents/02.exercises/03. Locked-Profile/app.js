function lockedProfile() {
    const profileElements = document.getElementsByClassName('profile');

    Array.from(profileElements).forEach(x => {
        const showMoreButtonElement = x.querySelector('button');
        
        showMoreButtonElement.addEventListener('click', ()=>{
            const hiddenFieldElement = x.querySelector('div[id]');
            const radioButtonValues = Array.from(x.querySelectorAll('input[type=radio]')).map(y=>y.checked)
            if (radioButtonValues[1] === true) {
                hiddenFieldElement.style.display = 
                    hiddenFieldElement.style.display==='block'?'none':'block';
                showMoreButtonElement.textContent = 
                    showMoreButtonElement.textContent==='Show more'?'Hide it':'Show more';
            }
        });
    });

    
}