import requests

# GET Avslisções
avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando os dados
print(avaliacoes.json())

# GET Avslisção
avaliacoe = requests.get('http://localhost:8000/api/v2/avaliacoes/1/')

# Acessando os dados
print(avaliacoe.json())


# GET Cursos
headers = {'Authorization': 'Token d5e90363593da660a4fe3a543b4dbfacfad2c150'}
cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.json())
