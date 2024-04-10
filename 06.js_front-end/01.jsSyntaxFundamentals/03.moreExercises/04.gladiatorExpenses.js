function solve(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice){
    let durability = {'helmet': 2, 'sword': 3, 'armor': 2}
    const maxDurability = {'helmet': 2, 'sword': 3, 'armor': 2}

    let totalPrice = 0;

    for (let i = 0; i < lostFights; i++){
        durability['helmet']-=1;
        durability['sword']-=1;

        const helmet = durability['helmet']==0;
        const sword = durability['sword']==0;
        const shield = helmet&&sword;

        if (shield) durability['armor']--;

        const armor = durability['armor']==0;

        if (helmet) {
            totalPrice += helmetPrice;
            durability['helmet'] = maxDurability['helmet'];
        }
        if (sword) {
            totalPrice += swordPrice;
            durability['sword'] = maxDurability['sword'];
        }
        if (shield) {
            totalPrice += shieldPrice;
        }
        if (armor) {
            totalPrice += armorPrice;
            durability['armor'] = maxDurability['armor'];
        }
    }
    
    console.log(`Gladiator expenses: ${totalPrice.toFixed(2)} aureus`);
}

solve(7,2,3,4,5);
solve(23,12.50,21.50,40,200);