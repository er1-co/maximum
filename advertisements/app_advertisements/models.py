from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Advertisement(models.Model):
    # Заголовок
    # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField('заголовок', max_length=128)
    # Описание
    description = models.TextField('описание')
    # Цена
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    # Торг
    auction = models.BooleanField('торг', help_text='Отметьте, если торг уместен')
    # Создание(дата, время)
    created_at = models.DateTimeField(auto_now_add=True)
    # Обновление
    updated_at = models.DateTimeField(auto_now=True)
    # пользователь
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    # изображение
    image = models.ImageField('изображение', upload_to='advertisements/')
