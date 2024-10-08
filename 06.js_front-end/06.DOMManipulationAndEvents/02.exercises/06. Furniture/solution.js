function solve() {
  document.querySelector('button:first-of-type').addEventListener('click', ()=>{
    const inputElement = document.querySelector('#exercise textarea');
    const newItemArray = JSON.parse(inputElement.value);
    const tbodyElement = Array.from(document.getElementsByClassName('table'))[0];

    newItemArray.forEach(x=>{
      const tr = document.createElement('tr');
      // x - obj
      for (const i of Object.values(x)){
        const td = document.createElement('td');
        if (i.startsWith('http')) {
          const img = document.createElement('img');
          img.src = i;
          td.appendChild(img);
        }
        else td.textContent = i;
        tr.appendChild(td);
      }
      const newInputElement = document.createElement('input');
      inputElement.type = 'checkbox';
      const td1 = document.createElement('td');
      td1.appendChild(newInputElement);
      tr.appendChild(td1);
      tbodyElement.appendChild(tr);
    });

  })
}