function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      Array.from(document.getElementsByClassName('select')).forEach(x => x.classList.remove('select'));
      const searchField = document.getElementById('searchField');
      const query = searchField.value;
      const rows = Array.from(document.querySelectorAll('tbody tr td')).filter(x=>x.textContent.includes(query))
      rows.forEach(x=>x.parentElement.classList.add('select'));
      searchField.value = '';
   }
}