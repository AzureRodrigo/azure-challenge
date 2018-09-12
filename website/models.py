from enum import Enum
from enumfields import EnumIntegerField
from django.db import models


# Enum de opções usado na inserção de novos registros
class EntryType(Enum):
    ENTRADA = True
    SAIDA = False


# Modelo de "dados" dos objetos da tabela registers
class Register(models.Model):
    class Meta:
        db_table = 'registers'

    name = models.EmailField()
    cost = models.FloatField()

    type = EnumIntegerField(
        enum=EntryType,
        default=EntryType.ENTRADA
    )

    def __str__(self):
        return self.name

