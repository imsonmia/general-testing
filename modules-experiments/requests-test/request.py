import requests
url = "https://www.bilibili.com"
response = requests.get(url)
response.encoding = 'utf-8'
print(response.text)
