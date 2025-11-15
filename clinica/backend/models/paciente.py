import uuid
from django.db import models
from usuario import Usuario
from endereco import Endereco


class Paciente(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    nome = models.CharField(blank=False, null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    cpf = models.CharField(max_length=11, blank=False, null=False, related_name='cpf')
    contato = models.CharField(default='sem telefone', null=False, related_name='contato')
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, blank=False, null=False, related_name='endereco')
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=False, null=False, related_name='user')


    def __str__(self):
        return f"Nome: {self.nome} Endereco: {self.endereco} Contato: {self.contato}"

