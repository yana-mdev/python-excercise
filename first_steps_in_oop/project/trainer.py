from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: list[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        pokemon = next((p for p in self.pokemons if p.name == pokemon_name), None)
        if pokemon is not None:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        pokemon_data = [f"Pokemon Trainer {self.name}",
                        f"Pokemon count {len(self.pokemons)}"]
        for pokemon in self.pokemons:
            pokemon_data.append(f"- {pokemon.pokemon_details()}")

        return "\n".join(pokemon_data)
