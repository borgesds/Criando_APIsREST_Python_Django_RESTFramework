import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

# print(resultados)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')

# print(nome)

# Todos os nomes das pessoas que avaliarao
# nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')

# print(nomes)

# Todos as avaliações
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')

print(notas)
