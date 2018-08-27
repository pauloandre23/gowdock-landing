from django.db import models

# Create your models here.

class CadastroLanding(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return "%s - %s" % (self.nome,self.email)
