# Gregory Vincent
# gvincent@Jjahnelgroup.com
# 6/19/23
# Code for Testing the API
import requests




BASE_URL = "http://127.0.0.1:5000/"


choice = input("Enter GET or POST")
if choice.upper() == "GET":
    searchName = input("What would you like to search for? ")
    if isinstance(searchName, str):
        response = requests.get(f"{BASE_URL}getNameData/{searchName.lower()}")
        if response.status_code == 200:
            print(response.json())
    else:
        print("Name doesn't exist in JSON File.")



 




    