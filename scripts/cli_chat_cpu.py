import requests

URL = "http://127.0.0.1:8000/get_recipe"

while True:
    ing = input("Enter ingredients (comma separated) or 'exit': ")
    if ing.lower() in ["exit", "quit"]:
        break
    ingredients = [x.strip() for x in ing.split(",")]
    resp = requests.post(URL, json={"ingredients": ingredients})
    print("\nRecipe:\n", resp.json()["recipe"], "\n")
