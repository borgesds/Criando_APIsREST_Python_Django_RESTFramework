from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de Cursos
    """
    def get(self, request):
        # buscar todos os cursos
        cursos = Curso.objects.all()
        # passar o parametro que esta buscando todos
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        # pegar os dados
        serializer = CursoSerializer(data=request.data)
        # verificar se são validos e salvar
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # retorna os dados salvo e o status HTTP
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API de Avaliação dos cursos
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
 