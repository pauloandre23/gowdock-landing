from django.db import models

# Create your models here.

class CadastroLanding(models.Model):
    nome = models.CharField(
        max_length=120,
        error_messages={
            'blank': "Nome vazio"
        }
    )
    email = models.EmailField(
        unique=True,
        error_messages={
            'null': "Email nulo",
            'blank': "Email vazio",
            'invalid': "Email inválido",
            'unique': "Email já cadastrado"
        }
    )

    def __str__(self):
        return "%s - %s" % (self.nome,self.email)
