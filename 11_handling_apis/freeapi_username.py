import requests
import random

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    requests.get(url)
    response = requests.get(url)
    data = response.json()
    # print(data)
    if data ["success"] and "data" in data:
        users = data["data"]["data"]
        user_data = random.choice(users)
        username = user_data["login"] ["username"]
        country = user_data["location"] ["country"]
        return username, country
    else:
        raise Exception("Faild to fetch user data")
    
def main():
    try:
        username, country = fetch_random_user()
        print(f"Username : {username}\nCountry = {country}")
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    main()
    