function generateReport() {
    const outputElement = document.getElementById('output')
    const thElements = Array.from(document.querySelectorAll('th'))
        .map(th => {
            const checkboxElement = th.querySelector('input');

            return {
                name: th.textContent.trim().toLowerCase(),
                checked: checkboxElement.checked
            };
        });
    
    const trElements = Array.from(document.querySelectorAll('tbody tr'));
    const res = [];
    trElements.forEach(x => {
        const tdElements = Array.from(x.children);

        const obj = {}
        tdElements.forEach((y, i) => {
            if (thElements[i].checked)
                obj[thElements[i].name] = y.textContent;
        });
        res.push(obj);
    });

    outputElement.textContent = JSON.stringify(res, null, 2);
}