function solve() {
  let func;
  switch (document.getElementById('naming-convention').value){
    case 'Camel Case':
      func = (text) => text.split(' ')[0].toLowerCase() + text.split(' ').slice(1).map(x => x.charAt(0).toUpperCase() + x.slice(1).toLowerCase()).join('');
      break;
    case 'Pascal Case':
      func = (text) => text.split(' ').map(x => x.charAt(0).toUpperCase() + x.slice(1).toLowerCase()).join('');
      break;
    default:
      func = (text) => 'Error!';
      break;
  }
  document.getElementById('result').textContent = func(document.getElementById('text').value)
}
