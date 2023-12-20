from django.db import models


class Patient(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    surname = models.CharField(verbose_name='Отчество', max_length=100)
    email = models.EmailField(unique=True, verbose_name='Почта')

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self):
        return f'{self.first_name}{self.last_name}{self.surname}'
