import requests

def getWeather():
    city = input("Enter city name: ")
    key = "c726c328b68da1dd57231b76a50eaf12"
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    response = requests.get(api)
    data = response.json()
    temp = round(data['main']['temp'] - 273.15, 2)
    print("")
    print("Name of the city: "+ data['name'])
    print("Temperature:", temp, "°C")
    print("Humidity:", data['main']['humidity'], "%")
    print("Wind speed:", data['wind']['speed'], "km/h")
    print("")

print("Welcome to the weather app")
start = True
while start:
    op = input("Do you want to know the weather? (y/n) : ")
    if op == 'y':
        getWeather()
    elif op == 'n':
        start = False
        print("Thank you for using the weather app")