from django.db import models


# Create your models here.
class User(models.Model):
    nickname = models.CharField('Никнейм', max_length=30)
    password = models.CharField('Пароль', max_length=30)
    registration_date = models.DateField('Дата регистрации', auto_now_add=True)

    def __str__(self):
        return self.nickname


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
    post_date_time = models.DateTimeField('Дата и время публикации', auto_now_add=True)

    def __str__(self):
        return self.title
