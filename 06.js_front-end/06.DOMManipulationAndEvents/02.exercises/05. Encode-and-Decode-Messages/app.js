function encodeAndDecodeMessages() {
    const sendButtonElement = document.querySelector('#main div:first-of-type button');
    const receiveButtonElement = document.querySelector('#main div:last-of-type button');

    const sendTextElement = document.querySelector('#main div:first-of-type textarea');
    const receiveTextElement = document.querySelector('#main div:last-of-type textarea');
    
    sendButtonElement.addEventListener('click', () => {
        let text = sendTextElement.value;
        let newText = '';
        for (let i = 0; i < text.length; i++) {
            newText += String.fromCharCode(text.charCodeAt(i)+1);
        }

        receiveTextElement.value = newText;
        sendTextElement.value = '';
    })

    receiveButtonElement.addEventListener('click', ()=>{
        let text = receiveTextElement.value;
        let newText = '';
        for (let i = 0; i < text.length; i++) {
            newText += String.fromCharCode(text.charCodeAt(i)-1);
        }

        receiveTextElement.value = newText;
    })
}