import requests

data = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json").json()
print(f"Bitcoin Price: ${data['bpi']['USD']['rate']}")
