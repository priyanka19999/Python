import requests
import random


def api():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    requests.get(url)
    response = requests.get(url)
    data = response.json()
    
    if data ["success"] and "data" in data:
        jokes = data['data'] ['data']
        jokes_data = random.choice(jokes)
        category = jokes_data["content"] 
        category_id = jokes_data["id"]
        return category, category_id
    else:
        raise Exception("Faild to fetch user data")
    
def main():
    try:
        category,category_id = api()
        print(f'Category = {category}\nCategoryId = {category_id}')
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()