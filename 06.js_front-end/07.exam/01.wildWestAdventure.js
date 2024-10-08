function solve(arr){
    const n = Number(arr[0]);
    const characters = [] // { name, hp, bullets }
    for (let i = 0; i < n; i++){
        const text = arr[i+1].split(' '); // charname hp[max100] bullets
        characters.push({
            name: text[0],
            hp: Number(text[1]),
            bullets: Number(text[2])
        })
    }

    for (let i = n; i < arr.length; i++){
        let currentCommand = arr[i].split(' - ')
        const charName = currentCommand[1];
        const char = characters.filter(x=>x.name===charName)[0];
        switch (currentCommand[0]){
            case 'FireShot':
                const target = currentCommand[2];
                if (char.bullets>0) {
                    char.bullets--;
                    console.log(`${charName} has successfully hit ${target} and now has ${char.bullets} bullets!`);
                } else {
                    console.log(`${charName} doesn't have enough bullets to shoot at ${target}!`);
                }
                break;

            case 'TakeHit':
                const damage = Number(currentCommand[2]);
                const attacker = currentCommand[3];
                
                char.hp -= damage;
                if (char.hp > 0) console.log(`${charName} took a hit for ${damage} HP from ${attacker} and now has ${char.hp} HP!`);
                else {
                    console.log(`${charName} was gunned down by ${attacker}!`);
                    characters.splice(characters.indexOf(char), 1);
                }
                break;

            case 'Reload':
                if (char.bullets === 6) console.log(`${charName}'s pistol is fully loaded!`);
                else console.log(`${charName} reloaded ${6-char.bullets} bullets!`);
                char.bullets = 6;
                break;

            case 'PatchUp':
                const amount = Number(currentCommand[2]);
                if (char.hp === 100) { console.log(`${charName} is in full health!`); break; }
                const oldHp = char.hp;
                char.hp += amount;
                if (char.hp > 100) char.hp = 100;
                console.log(`${charName} patched up and recovered ${char.hp - oldHp} HP!`);
                break;
            default: break;
        }
    }

    characters.forEach(x => {
        console.log(`${x.name}\n HP: ${x.hp}\n Bullets: ${x.bullets}`);
    });
}

// solve(["2","Gus 100 0","Walt 100 6","FireShot - Gus - Bandit","TakeHit - Gus - 100 - Bandit","Reload - Walt","Ride Off Into Sunset"])
// solve(["2","Jesse 100 4","Walt 100 5","FireShot - Jesse - Bandit","TakeHit - Walt - 30 - Bandit","PatchUp - Walt - 20" ,"Reload - Jesse","Ride Off Into Sunset"])
// solve(["2","Gus 100 4","Walt 100 5","FireShot - Gus - Bandit","TakeHit - Walt - 100 - Bandit","Reload - Gus","Ride Off Into Sunset"]);