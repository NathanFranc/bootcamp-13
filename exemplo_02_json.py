import requests
import json
from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    types: str  # Como string separada por vírgulas

def pegar_pokemon(id: int) -> PokemonSchema:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    
    # Salvar em arquivo
    with open(f"{data['name']}.json", 'w') as f:
        json.dump(data, f, indent=2)
    
    # Extrair tipos
    types_list = []
    for type_info in data['types']:
        types_list.append(type_info['type']['name'])
    
    types_str = ', '.join(types_list)
    return PokemonSchema(name=data['name'], types=types_str)

# Executar
pokemon = pegar_pokemon(24)
print(pokemon)