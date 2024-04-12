function search() {
   const query = document.getElementById('searchText').value;
   const listItems = Array.from(document.querySelectorAll('#towns li')).filter(x => x.textContent.includes(query))

   listItems.forEach(x => {
      x.style.textDecoration = 'underline';
      x.style.fontWeight = 'bold';
   })
   
   document.getElementById('result').textContent = listItems.length + " matches found";
}
