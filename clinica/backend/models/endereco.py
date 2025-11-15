import uuid
from django.db import models


class Endereco(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    municipio = models.CharField(blank=False, null=False, related_name='municipio')
    bairro = models.CharField(blank=False, null=False, related_name='bairro')
    rua = models.CharField(blank=False, null=False, related_name='rua')
    numero = models.CharField(blank=False, null=False, related_name='numero')

    def __str__(self):
        return f"Endereco: {self.municipio}-{self.bairro}, {self.rua}, {self.numero}"

