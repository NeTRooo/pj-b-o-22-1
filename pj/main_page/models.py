from django.db import models

# user, nick, access, prime, pay, pay_id
class Disciplines(models.Model):

    discipline = models.TextField(verbose_name='Предмет')
    actualhomework = models.TextField(verbose_name='Актуальное дз')

    class Meta:
        verbose_name = 'Актуальное дз'
        verbose_name_plural = 'Актуальные дз'
