"""
Need requests library
py -m pip install --user requests
"""

import requests
url ="https://api.openweathermap.org/data/2.5/weather?q=" 
area = input("Enter the area: ")
x = url + area + "&appid=853682ff0c20771bdf12db82dc461ab2"
r = requests.get(x)
data = r.json()
print(data)
