from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        # não sera mostrado na hora da consulta
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    # Aqui mandamos todas as avalições para leitura de uma vez
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    """
    # HyperLinked Related Field
    avaliacoes = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail'
    )
    """

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'  # adciona a variavelcriada acima
        )
