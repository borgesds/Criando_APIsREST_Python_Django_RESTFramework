import requests

headers = {'Authorization': 'Token d5e90363593da660a4fe3a543b4dbfacfad2c150'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

# print(resultado.json())

# Testando se esta correto
assert resultado.status_code == 200

# Testando a quantida de registros
assert resultado.json()['count'] == 4

# Testando se o titulo do primeiro curso esta correto
assert resultado.json()['results'][0]['tilulo'] == 'Criação de APIs REST com Django REST Framework'

