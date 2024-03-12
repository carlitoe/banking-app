import requests

while True:
    chosen_pokemon = input("Please enter your pokemon of choice: ").capitalize()
    pokemon = f"https://pokeapi.co/api/v2/pokemon/{chosen_pokemon}".lower()
    req = requests.get(pokemon)

    if req.status_code == 200:
        data = req.json()
        print(f"You have chosen: {chosen_pokemon}")
        print(f"{chosen_pokemon}'s weight is: {data['weight']}")
        print(f"{chosen_pokemon}'s base experience is: {data['base_experience']}")
        print(f"{chosen_pokemon}'s height is: {data['height']}")


        for ability in data['abilities']:
            req = requests.get(ability['ability'] ['url'])
            ability_data = req.json()
            ability_name = ability_data['name']
            print(f"Abilities: {ability_name}")

        """for move in data['moves']:
            req = requests.get(move['move']['url'])
            move_data = req.json()
            move_name = move_data['name']
            print(f"Pokemon's moves: {move_name}")"""

        for form in data['forms']:
            req = requests.get(form['url'])
            p_forms = req.json()
            poke_form = p_forms['name']
            print(f"Pokemon's forms: {poke_form}")

    else:
        print("Pokemon not found")
   