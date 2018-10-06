from rest_framework import serializers
from django.core.validators import MinValueValidator

from api.models import Register, EntryType
from api import fields


# Serializer dos registros
class RegisterSerializer(serializers.ModelSerializer):

    # mantive a nomenclatura o mais próxima do documento que me foi passado
    tipo_de_registro = fields.EnumField(enum=EntryType, write_only=True, source='type')
    nome_do_registro = serializers.CharField(max_length=200, source='name')
    valor_em_reais = serializers.DecimalField(source='cost',
                                              decimal_places=2,
                                              max_digits=12,
                                              validators=[MinValueValidator(0.01)]
                                              )

    # registra os campos na "view"
    class Meta:
        model = Register
        fields = ('tipo_de_registro', 'nome_do_registro', 'valor_em_reais')

    # ao inserir um novo elemento define se o valor é negativo ou positivo.
    def create(self, validated_data):
        name = validated_data['name']
        cost = validated_data['cost']
        is_entry = validated_data['type'].value
        if not is_entry:
            cost = cost * -1

        return Register.objects.create(name=name, cost=float(cost), type=is_entry)
