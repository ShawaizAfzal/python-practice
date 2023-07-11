import requests

def sum_numbers(num1, num2):
    url = "http://127.0.0.1:5000/"  # Replace with the actual URL of your API

    params = {
        "num1": num1,
        "num2": num2
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            result = response.json()
            print(result)
        else:
            print("Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
sum_numbers(num1=10,num2=20)

