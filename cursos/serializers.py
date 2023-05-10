from rest_framework import serializers
from django.db.models import Avg

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

    def validate_avaliacao(self, valor):  # validate_xxx campo de valiação
        if valor in range(1, 6):  # so vai ter notas de 1 a 5
            return valor
        raise serializers.ValidationError('A avaliação precisa ser entre 1 e 5')


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

    # media de avaliações
    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',  # adciona a variavelcriada acima
            'media_avaliacoes'
        )

    # função media
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2








