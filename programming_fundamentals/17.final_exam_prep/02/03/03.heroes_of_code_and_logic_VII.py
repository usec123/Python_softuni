MAX_HP = 100
MAX_MP = 200

n = int(input())

heroes = {}

for _ in range(n):
    hero = input().split()
    name = hero[0]
    hp = int(hero[1])
    mp = int(hero[2])

    if hp<=MAX_HP and mp<=MAX_MP:
        heroes[name] = [hp,mp]

cmd = input()
while cmd!='End':
    cmd = cmd.split(' - ')
    
    if cmd[0] == 'CastSpell':
        hero = cmd[1]
        mp_needed = int(cmd[2])
        spell_name = cmd[3]
        
        if heroes[hero][1] >= mp_needed:
            heroes[hero][1]-=mp_needed
            print(f'{hero} has successfully cast {spell_name} and now has {heroes[hero][1]} MP!')
        else:
            print(f'{hero} does not have enough MP to cast {spell_name}!')
    
    elif cmd[0] == 'TakeDamage':
        hero = cmd[1]
        dmg = int(cmd[2])
        attacker = cmd[3]

        heroes[hero][0]-=dmg
        if heroes[hero][0]>0:
            print(f'{hero} was hit for {dmg} HP by {attacker} and now has {heroes[hero][0]} HP left!')
        else:
            heroes.pop(hero)
            print(f'{hero} has been killed by {attacker}!')
    
    elif cmd[0] == 'Recharge':
        hero = cmd[1]
        amount = int(cmd[2])
        
        old_mp = heroes[hero][1]
        heroes[hero][1] += amount
        if heroes[hero][1] > MAX_MP:
            heroes[hero][1] = MAX_MP
        print(f'{hero} recharged for {heroes[hero][1]-old_mp} MP!')
        
    
    elif cmd[0] == 'Heal':
        hero = cmd[1]
        amount = int(cmd[2])
        
        old_hp = heroes[hero][0]
        heroes[hero][0] += amount
        if heroes[hero][0] > MAX_HP:
            heroes[hero][0] = MAX_HP
        print(f'{hero} healed for {heroes[hero][0]-old_hp} HP!')
    
    cmd = input()

for key,value in heroes.items():
    print(key)
    print(f'  HP: {value[0]}')
    print(f'  MP: {value[1]}')