from django.db import models
from users.models import CustomUser

class Feriados(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data = models.DateField()
    description = models.CharField(max_length=200, default='Não especificado')

    def __str__(self):
        return self.data

    class Meta:
        db_table = 'tb_feriados'