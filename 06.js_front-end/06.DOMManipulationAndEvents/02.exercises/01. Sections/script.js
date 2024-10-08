function create(words) {
   words.forEach(x=>{
      const currentElement = document.createElement('div');
      
      const paraElement = document.createElement('p');
      paraElement.textContent = x;
      paraElement.style.display='none';
      
      currentElement.appendChild(paraElement);
      
      currentElement.addEventListener('click', () => currentElement.querySelector('p').style.display='block');
      
      document.getElementById('content').appendChild(currentElement);
   })
}