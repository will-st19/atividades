import json

print('Manipula JSON')

with open('webmotor.json', encoding='utf8') as f:
    jsondata = json.load(f)

# print(jsondata['NewSearchResults'][0]['make'], end=' ')
# print(jsondata['NewSearchResults'][0]['model'], end=" ")
# print(jsondata['NewSearchResults'][0]['year'], end=" ")
# print(jsondata['NewSearchResults'][0]['price'])

for carro in jsondata['NewSearchResults']:
    nome = carro['make']
    marca = carro['model']
    ano = carro['year']
    preco = carro['price']
    local = carro['location']
    print('/*' * 30)
    print(f'({nome}', f'{marca})', f'| {ano} |', f'{preco} |', f'({local})')