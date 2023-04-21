# Generated by Django 4.2 on 2023-04-20 23:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='subscriptions',
            field=models.ManyToManyField(related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
        migrations.AlterField(
            model_name='account',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='account',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Личная информация'),
        ),
    ]