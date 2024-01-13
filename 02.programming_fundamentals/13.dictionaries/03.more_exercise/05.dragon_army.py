dragons = {} # type : [Dragon]
default_values = {'damage':45,'health':250,'armor':10}

class Dragon:
    def __init__(self,_name,_damage,_health,_armor):
        self.name = _name
        self.damage = int(_damage) if _damage!='null' else 45
        self.health = int(_health) if _health!='null' else 250
        self.armor = int(_armor) if _armor!='null' else 10
    
    def __repr__(self) -> str:
        return \
            f'-{self.name} -> damage: {self.damage}, health: {self.health}, armor: {self.armor}'

def average_stats(_type):
    avg_damage = 0
    avg_health = 0
    avg_armor = 0
    for dragon in dragons[_type]:
        avg_damage += dragon.damage
        avg_health += dragon.health
        avg_armor += dragon.armor
    avg_damage /= len(dragons[_type])
    avg_health /= len(dragons[_type])
    avg_armor /= len(dragons[_type])
    return f'{avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f}'

n = int(input())
for _ in range(n):
    type,name,damage,health,armor = input().split()
    if type not in dragons:
        dragons[type] = []
    if name not in [dragons[type][x].name for x in range(len(dragons[type]))]:
        dragons[type].append(Dragon(name,damage,health,armor))
    else:
        dragons[type][\
            [dragons[type][x].name for x in range(len(dragons[type]))].index(name)\
                ] = Dragon(name,damage,health,armor)

for type,dragon_list in dragons.items():
    print(f'{type}::({average_stats(type)})')
    dragon_list = sorted(dragon_list,key=lambda x: x.name)
    for dragon in dragon_list:
        print(dragon)