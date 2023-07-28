from django.db import models
from users.models import CustomUser

class Feriado(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return self.data

    class Meta:
        db_table = 'tb_feriados'