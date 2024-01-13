import re

health_pattern = r'[^0-9\+\-\*/\.]'
damage_pattern = r'[\+\-]?[0-9]+\.?[0-9]*'
damage_multiplier_pattern = r'[\*/]'

class Demon:
    def __init__(self,name):
        self._name = name
        self.calculate_hp()
        self.calculate_dmg()
    
    def calculate_hp(self):
        self._hp = sum([ord(x) for x in re.findall(health_pattern,self._name)])
    
    def calculate_dmg(self):
        dmg = sum([float(x) for x in re.findall(damage_pattern,self._name)])
        for multiplier in re.findall(damage_multiplier_pattern, self._name):
            if multiplier == '*':
                dmg*=2
            else:
                dmg/=2
        self._dmg = dmg
    def __repr__(self):
        return f'{self._name} - {self._hp} health, {self._dmg:.2f} damage'

demons = [Demon(demon) for demon in sorted([str.strip(x) for x in input().split(',')])]
for demon in demons: print(demon)