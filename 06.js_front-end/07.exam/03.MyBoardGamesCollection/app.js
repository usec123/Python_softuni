function solve(){


const loadAllGamesButton = document.getElementById('load-games');
const boardGameListElement = document.getElementById('games-list');

loadAllGamesButton.addEventListener('click', ()=>{
    Array.from(boardGameListElement.children).forEach(x=>x.remove())
    fetch('http://localhost:3000/server/data/games')
    .then((response) => response.json())
    .then((json) => Array.from(Object.values(json)).forEach(x => {
        // x = dict - name, players, type
        const divBoardGameElement = document.createElement('div');
        const divContentElement = document.createElement('div');
        const pNameElement = document.createElement('p');
        const pPlayersElement = document.createElement('p');
        const pTypeElement = document.createElement('p');
        const divButtonsElement = document.createElement('div');
        const buttonChangeElement = document.createElement('button');
        const buttonDeleteElement = document.createElement('button');
        
        divBoardGameElement.classList.add('board-game');
        divContentElement.classList.add('content');
        divButtonsElement.classList.add('buttons-container');
        buttonChangeElement.classList.add('change-btn');
        buttonDeleteElement.classList.add('delete-btn');
        
        pNameElement.textContent = x['name'];
        pTypeElement.textContent = x['type'];
        pPlayersElement.textContent = x['players'];
        buttonChangeElement.textContent = 'Change';
        buttonDeleteElement.textContent = 'Delete';
        
        divContentElement.appendChild(pNameElement);
        divContentElement.appendChild(pTypeElement);
        divContentElement.appendChild(pPlayersElement);
        
        divButtonsElement.appendChild(buttonChangeElement);
        divButtonsElement.appendChild(buttonDeleteElement);
        
        divBoardGameElement.appendChild(divContentElement);
        divBoardGameElement.appendChild(divButtonsElement);
        
        boardGameListElement.appendChild(divBoardGameElement);
    }));
})

const addGameButton = document.getElementById('add-game');
const nameElement = document.getElementById('g-name');
const typeElement = document.getElementById('type');
const playersElement = document.getElementById('players');

addGameButton.addEventListener('click', ()=>{
    const data = {
        name: nameElement.value,
        type: typeElement.value,
        players: playersElement.value,
    }


    fetch('http://localhost:3000/jsonstore/games', {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify(data),
    })
    .then(() => {
        loadAllGamesButton.click();

        nameElement.value = '';
        typeElement.value = '';
        playersElement.value = '';
    })
});
}
solve();