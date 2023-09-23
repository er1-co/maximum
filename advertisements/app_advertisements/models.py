from django.db import models

# Create your models here.


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

    # class Meta:
    #     db_table = 'advertisements'
    #
    # def __str__(self):
    #     return f'<Advertisement(id={self.id}, title={self.title}, price={self.price})>'
