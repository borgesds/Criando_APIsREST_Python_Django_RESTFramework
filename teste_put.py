import requests

headers = {'Authorization': 'Token 3f650c7bf0f7db344b5da4b4dc26148a1cfce444'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Django para API Rest 3",
    "url": "https://www.udemy.org/?gclid=Cj0KCQjwpPKiBhDvARIsACn-gzBDFtV2J82ZV"
}

# Buscando o curso id 1
# curso = requests.get(url=f'{url_base_cursos}1/', headers=headers)
# print(curso.json())


resultado = requests.put(url=f'{url_base_cursos}1/', headers=headers, data=curso_atualizado)

# Testando o status HTTP
assert resultado.status_code == 200

# Testando o titulo
assert resultado.json()['titulo'] == curso_atualizado['titulo']
