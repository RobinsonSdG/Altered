import requests
import json

def get_card(name, rarity):
    url = f"https://api.altered.gg/cards"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        for card in data["hydra:member"]:
            # print(card)
            match rarity:
                case "common":
                    if card["name"] == name and card["@id"].endswith("C"):
                        return card["elements"]
                case "rare":
                    if card["name"] == name and card["@id"].endswith("R1"):
                        return card["elements"]
                case "oof":
                    if card["name"] == name and card["@id"].endswith("R2"):
                        return card["elements"]
        return "not found"
    else:
        print(f"La requête pour la carte {name} a échoué avec le code de statut {response.status_code}")
        return []
    
def main():
    name = input("Enter card name: ")
    print ("Card name".format(name))
    rarity = input("Enter card rarity: ")
    print ("Card rarity (common, rare, oof)".format(rarity))
    print(get_card(name, rarity))

main()