from django.db import models

# discipline, eng_discipline
class Disciplines(models.Model):

    discipline = models.TextField(verbose_name='Предмет')
    eng_discipline = models.TextField(verbose_name='Предмет на англ')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
    
    def __str__(self):
        return self.discipline

# discipline, eng_discipline, actual_homework, actual_file
class DisciplinesActual(models.Model):

    discipline = models.ForeignKey(Disciplines, on_delete=models.CASCADE,verbose_name='Домашка какого предмета')
    eng_discipline = models.TextField(verbose_name='Предмет на англ')
    actual_homework = models.TextField(verbose_name='Актуальное дз')
    actual_file = models.FileField(upload_to='homework', verbose_name='Дз файл', null=True, blank=True)
    date = models.DateField(verbose_name='Дата дз')

    class Meta:
        verbose_name = 'Актуальное дз'
        verbose_name_plural = 'Актуальные дз'
    
    def __str__(self):
        return self.eng_discipline

# discipline, eng_discipline, actual_homework, actual_file
class DisciplineHomeWork(models.Model):

    discipline = models.ForeignKey(Disciplines, on_delete=models.CASCADE,verbose_name='Домашка какого предмета')
    eng_discipline = models.TextField(verbose_name='Предмет на англ')
    actual_homework = models.TextField(verbose_name='Дз')
    actual_file = models.FileField(upload_to='homework', verbose_name='Дз файл', null=True, blank=True)
    date = models.DateField(verbose_name='Дата дз')

    class Meta:
        verbose_name = 'Все дз'
        verbose_name_plural = 'Все дз'
    
    def __str__(self):
        return self.eng_discipline
