from django.db import models

class Corrente(models.Model):
    titulo = models.CharField(max_length=50,
                              null=False,
                              blank=False,
                              verbose_name='Título Corrente',
                              )

    corrente = models.TextField(max_length=5000,
                                null=False,
                                blank=False,
                                verbose_name='Corrente',
                                )

    disponivel = models.BooleanField(default=True,
                                     verbose_name='Disponível',
                                     )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Corrente'
        verbose_name_plural = 'Correntes'

