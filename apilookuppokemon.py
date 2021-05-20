#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com"""

# python3 -m pip install requests
import requests

def main():

    poke = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

    # display the JSON attached to the 200 response
    pokedata = poke.json()
    # confirm we have a dict
    print(type(pokedata))

    # display only the keys within the dict
    print(pokedata.keys())

    print(pokedata.get("game_indices"))

    # assign the list of games to games
    games = pokedata.get("game_indices")

    for game in games:
        game_nameurl = game.get("version")

        print("That pokemon appears in the game:")
        print("\t" + game_nameurl.get("name").capitalize())
        print("\t" + game_nameurl.get("url"))







if __name__ == "__main__":
    main()
