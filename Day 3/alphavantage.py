import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=XX4NCYLTBFSGKZ18'
r = requests.get(url)
status = r
print(status)
data = r.json()
print(data)