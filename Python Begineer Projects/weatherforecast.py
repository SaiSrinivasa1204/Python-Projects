import requests

city = input('Please enter the city name: ')
print(city)

print("The weather report for:" + city)

url = 'https://wttr.in/{}'.format(city)

res = requests.get(url)
print(res.text)