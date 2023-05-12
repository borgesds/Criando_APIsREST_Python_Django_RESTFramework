import requests


class TestCursos:
    headers = {'Authorization': 'Token 3f650c7bf0f7db344b5da4b4dc26148a1cfce444'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programação com Ruby",
            "url": "http://www.geekuniversity.com.br/cpr"
        }

        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizacao = {
            "ttulo": "Novo Curso de Ruby Tipo2.3",
            "url": "http://www.geekuniversity.com.br/cpr23"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizacao)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizacao['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}3/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0


