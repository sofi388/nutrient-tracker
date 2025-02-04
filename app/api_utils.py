# app/api_utils.py
import requests

def fetch_food_names(food_name):
    """Fetch list of meal names by ingredient."""
    base_url = "https://www.themealdb.com/api/json/v1/1/filter.php"
    params = {"i": food_name}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        # Extract meal names
        return [meal["strMeal"] for meal in data.get("meals", [])]
    else:
        raise ValueError(f"API Error: {response.status_code} {response.text}")


if __name__ == "__main__":
    meal_names = fetch_food_names("chicken_breast")
    print(meal_names)