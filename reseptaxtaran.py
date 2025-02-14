import requests

def get_recipes(ingredients):
    api_key = "your_api_key_here"
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={','.join(ingredients)}&apiKey={api_key}"

    response = requests.get(url).json()
    
    if response:
        print(f"Found {len(response)} recipes based on your ingredients.")
        for idx, recipe in enumerate(response, start=1):
            print(f"{idx}. {recipe['title']}")
            print(f"   Link: https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-')}-{recipe['id']}")
    else:
        print("No recipes found with these ingredients.")

ingredients = input("Enter ingredients separated by commas: ").split(',')
get_recipes(ingredients)
