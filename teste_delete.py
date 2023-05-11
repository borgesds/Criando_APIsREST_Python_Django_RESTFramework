import requests

headers = {'Authorization': 'Token 3f650c7bf0f7db344b5da4b4dc26148a1cfce444'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

# Testando o status HTTP
assert resultado.status_code == 204

assert len(resultado.text) == 0
