# Generated by Django 3.2.8 on 2021-11-09 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30, verbose_name='Никнейм')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
                ('registration_date', models.DateField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('post_date_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forumapp.user', verbose_name='Автор')),
            ],
        ),
    ]
