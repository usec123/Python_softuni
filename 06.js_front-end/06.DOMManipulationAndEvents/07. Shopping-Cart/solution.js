function solve() {
   const outputElement = document.querySelector('.shopping-cart textarea');
   const items = {};
   let totalPrice = 0;

   Array.from(document.getElementsByClassName('product')).forEach(x => {
      x.querySelector('.product-add .add-product').addEventListener('click', () => {
         outputElement.value +=
         `Added ${x.querySelector('.product-title').textContent} for ${Number(x.querySelector('.product-line-price').textContent).toFixed(2)} to the cart.\n`;
         items[x.querySelector('.product-title').textContent] = true;
         totalPrice += Number(x.querySelector('.product-line-price').textContent);
      });
   })

   const pattern = /\bAdded (\w+) for ([0-9.]+) to the cart\./gim;
   const checkoutButtonElement = document.querySelector('.checkout').addEventListener('click', (event)=>{
      outputElement.value += `You bought ${Array.from(Object.keys(items)).join(', ')} for ${totalPrice.toFixed(2)}.`;
      Array.from(document.querySelectorAll('.product-add .add-product')).forEach(x => x.setAttribute('disabled', 'disabled'));
      event.target.setAttribute('disabled', 'disabled');
   });
}