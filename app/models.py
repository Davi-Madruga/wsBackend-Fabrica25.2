from django.db import models

class Pokemon(models.Model):
    id_pokemon = models.IntegerField()
    nome = models.CharField()
    tipos = models.CharField()
    altura = models.IntegerField()
    peso = models.IntegerField()


    def __str__(self):
        return f"#{self.id_pokemon}|{self.nome}"
    
class Ataque(models.Model):
    pokemon = models.ForeignKey(Pokemon,on_delete=models.CASCADE)
    id_ataque = models.IntegerField()
    nome = models.CharField()
    tipo = models.CharField()
    pp = models.CharField()
    power = models.CharField()
    accuracy = models.CharField()

    def __str__(self):
        return self.nome
