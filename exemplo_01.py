import requests
from pydantic import BaseModel  # CORREÇÃO: pydantic, não pydamtic

class PokemonSchema(BaseModel):
    name: str  # CORREÇÃO: name deve ser string, não int
    types: str  # CORREÇÃO: types (plural)

    class Config:
        from_attributes = True  # CORREÇÃO: from_attributes em vez de own_mode

def pegar_pokemon(id: int) -> PokemonSchema:  # CORREÇÃO: id, não td
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")  # CORREÇÃO: {id}
    data = response.json()
    print(data)
    
    data_types = data['types']
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    
    types = '; '.join(types_list)
    return PokemonSchema(name=data['name'], types=types)  # CORREÇÃO: types=types

# CORREÇÃO: Removido o import duplicado
pokemon = pegar_pokemon(24)
print(pokemon)