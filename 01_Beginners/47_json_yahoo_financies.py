import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/"
             "quote?format=json") as response:
    source = response.read()

# 1
# print(source)

#2
data = json.loads(source)

#print(json.dumps(data, indent=2))

# 3 Counting resources
# print(len(data['list']['resources']))

# 4 verificando resources
# for item in data['list']['resources']:
#     #print(item)
#     name = item['resource']['fields']['name']
#     price = item['resource']['fields']['price']
#     print(name, price)


# 5 criando um dicionario vazio para salvar as conversões de moedas
usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

# print(usd_rates)
# print(usd_rates['USD/EUR'])
print(50 * float(usd_rates['USD/EUR']))
