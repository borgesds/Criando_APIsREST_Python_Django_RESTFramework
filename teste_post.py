import requests

headers = {'Authorization': 'Token d5e90363593da660a4fe3a543b4dbfacfad2c150'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerenciar Proetos commetodologia Agil Scrum",
    "url": "https://www.alura.com.br/formacao-gerente-agil?gclid=Cj0KCQjwpPKiBhDvARIsACn-gzAl3NGMBi0Vz1YeKNfu7O1g3l6pXs-hfGuFxTpivw5eU-5XN1bxDBkaAv4lEALw_wcB"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o codigo de status HTTP 201
assert resultado.status_code == 201

# Testando se o titulo do curso retornadoe o msminformdo
assert resultado.json()['titulo'] == novo_curso['titulo']

