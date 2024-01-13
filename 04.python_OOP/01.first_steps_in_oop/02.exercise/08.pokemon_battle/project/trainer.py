from .pokemon import Pokemon


class Trainer:
    def  __init__(self,name:str):
        self.name = name
        self.pokemons = []
    
    def add_pokemon(self, pokemon:Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        else:
            return 'This pokemon is already caught'
    
    def release_pokemon(self, pokemon_name:str):
        for x in range(len(self.pokemons)):
            if self.pokemons[x].name == pokemon_name:
                self.pokemons.pop(x)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        pokemon_details = "\n".join([f"- {pokemon.pokemon_details()}" for pokemon in self.pokemons])
        return (f'Pokemon Trainer {self.name}\n'
                f'Pokemon count {len(self.pokemons)}\n'
                f'{pokemon_details}')