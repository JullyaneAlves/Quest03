from django.db import models
from django.core.validators import RegexValidator

from django.contrib import admin

class ItemTema(models.Model):
        class Meta:
                verbose_name_plural = "Itens"

        nome = models.CharField('Nome', max_length=30)
        descricao = models.TextField('Descrição do Item')

        def __str__(self):
            return self.nome

class Tema(models.Model):
        class Meta:
              verbose_name_plural = "Temas"

        nome = models.CharField('Nome', max_length=30)
        valor = models.FloatField('Valor Aluguel')
        cor_toalha = models.ForeignKey(ItemTema, on_delete=models.CASCADE)

        def __str__(self):
            return self.nome

class Endereco(models.Model):
        class Meta:
                verbose_name_plural = "Endereços"

        logradouro = models.CharField('Logradouro', max_length=20)
        numero = models.IntegerField('Número')
        complemento = models.CharField('Complemento', max_length=30)
        bairro = models.CharField('Bairro', max_length=15)
        cidade = models.CharField('Cidade', max_length=15)
        uf = models.CharField('UF', max_length=2)
        cep_regex = RegexValidator(regex=r'^\+?1?\d{8,10}$', message="Cep number must be entered in the format: '64000000'. Up to 10 digits allowed.")
        cep = models.CharField(validators=[cep_regex], max_length=10, blank=True) # validators should be a list

        def __str__(self):
            return self.logradouro

class Cliente(models.Model):
        class Meta:
                verbose_name_plural = "Cliente"

        nome = models.CharField('Nome', max_length=30)
        fone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        fone = models.CharField(validators=[fone_regex], max_length=17, blank=True) # validators should be a list

        def __str__(self):
            return self.nome

class Aluguel(models.Model):
    data = models.DateField('Data da Festa')
    horainicio = models.TimeField('Hora Inicio')
    horatermino = models.TimeField('Hora Termino')
    valor = models.FloatField('Valor Total')
    temaescolhido = models.ForeignKey(Tema, on_delete=models.CASCADE)
    local = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Alugueis Agendados'
        verbose_name = 'Aluguel Agendado'
        ordering = ('-data', 'horainicio')
