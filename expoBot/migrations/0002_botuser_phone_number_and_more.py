# Generated by Django 4.2 on 2023-08-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expoBot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='phone_number',
            field=models.TextField(null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='botusercondition',
            name='on_phone_number_input',
            field=models.BooleanField(default=False, null=True, verbose_name='Ввод номера телефона'),
        ),
    ]