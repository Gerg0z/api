import requests
import random


def kulcsszo_alapjan(kulcs):
    url_kulcs = "https://icanhazdadjoke.com/search"
    headers = {
        "Accept": "application/json"
    }
    params = {
        "term": kulcs
    }
    kereso = requests.get(url_kulcs, headers=headers, params=params)
    if kereso.status_code == 200:
        data = kereso.json()
        if data["total_jokes"] > 0:
            return random.choice(data["results"])["joke"]
        else:
            return "Nincs ilyen vicc."
    return "Hiba."


def randomizalo():
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": "application/json"
    }
    kereso = requests.get(url, headers=headers)
    if kereso:
        return kereso.json().get("joke")
    return "Hiba."


def main():
    while True:
        kulcsszo = input("Adj meg egy angol szót a vicc kereséshez, ha üresen hagyod akkor random vicc lesz: ").strip()
        if kulcsszo:
            print("A szóval keresett vicc:")
            print(kulcsszo_alapjan(kulcsszo))
        else:
            print("A random vicc:")
            print(randomizalo())
        ujra = input("Szeretnél még egy viccet? (igen/nem): ").strip().lower()
        if ujra != "igen":
            print("Program vége")
            break


main()
