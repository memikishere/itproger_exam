from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField('Ссылка', max_length=200)
    link_name = models.CharField('Название', max_length=200)

    def __str__(self):
        return f'Логин: {self.user} | Ссылка: {self.link} | Имя ссылки: {self.link_name}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'