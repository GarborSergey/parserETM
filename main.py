import requests

url = 'https://www.etm.ru/catalog?page=1&searchValue=02140&type=code&rows=36'
article = '02140'

params = {
    'searchValue': article,
    'type': 'code',
    'page': 1,
    'rows': 36,
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
                  'Safari/537.36',
}

response = requests.get(url, headers=headers)
print(response.status_code)

with open('test.html', 'w') as file:
    file.write(response.text)