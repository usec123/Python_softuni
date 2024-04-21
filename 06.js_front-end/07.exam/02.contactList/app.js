window.addEventListener('load', solve)


function solve() {
  const nameElement = document.getElementById('name');
  const phoneNumberElement = document.getElementById('phone');
  const categoryElement = document.getElementById('category');
  const addButtonElement = document.getElementById('add-btn');
  const ulElement = document.getElementById('check-list');
  const contactUlElement = document.getElementById('contact-list');
  
  addButtonElement.addEventListener('click', ()=>{
    if (nameElement.value!==''&&phoneNumberElement.value!==''&&categoryElement.value!==''){
      const newLiElement = document.createElement('li');
      const articleElement = document.createElement('article');
      const p1Element = document.createElement('p');
      const p2Element = document.createElement('p');
      const p3Element = document.createElement('p');
      const divElement = document.createElement('div');
      const btn1Element = document.createElement('button');
      const btn2Element = document.createElement('button');
      const btn3Element = document.createElement('button');
      
      
      
      btn1Element.addEventListener('click', ()=>{
        nameElement.value = p1Element.textContent.split('name:')[1];
        phoneNumberElement.value = p2Element.textContent.split('phone:')[1];
        categoryElement.value = p3Element.textContent.split('category:')[1];
        
        newLiElement.remove();
      });
      
      btn2Element.addEventListener('click', ()=>{
        newLiElement.remove();
        
        btn1Element.remove();
        btn2Element.remove();
        divElement.appendChild(btn3Element);
        
        contactUlElement.appendChild(newLiElement);
      });
      
      btn3Element.addEventListener('click', ()=>{
        newLiElement.remove();
      })
      
      p1Element.textContent = `name:${nameElement.value}`;
      p2Element.textContent = `phone:${phoneNumberElement.value}`;
      p3Element.textContent = `category:${categoryElement.value}`;
      
      divElement.classList.add('buttons');
      btn1Element.classList.add('edit-btn');
      btn2Element.classList.add('save-btn');
      btn3Element.classList.add('del-btn');
      
      articleElement.appendChild(p1Element);
      articleElement.appendChild(p2Element);
      articleElement.appendChild(p3Element);
      
      divElement.appendChild(btn1Element);
      divElement.appendChild(btn2Element);
      
      newLiElement.appendChild(articleElement);
      newLiElement.appendChild(divElement);
      
      ulElement.appendChild(newLiElement);
      
      nameElement.value = '';
      phoneNumberElement.value = '';
      categoryElement.value = '';
    }
  })
}
