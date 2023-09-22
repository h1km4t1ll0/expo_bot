# Generated by Django 4.2 on 2023-08-14 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('telegram_id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID в телеграм')),
                ('nickname', models.TextField(verbose_name='Никнейм')),
                ('api_hash', models.TextField(null=True, verbose_name='Хеш для клиента ТГ')),
                ('api_id', models.TextField(null=True, verbose_name='API ID для клиента ТГ')),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Пользователь бота',
                'verbose_name_plural': 'Пользователи бота',
            },
        ),
        migrations.CreateModel(
            name='BotUserCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_api_hash_input', models.BooleanField(default=False, null=True, verbose_name='Ввод АПИ хеша')),
                ('on_api_id_input', models.BooleanField(default=False, null=True, verbose_name='Ввод ID АПИ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='expoBot.botuser')),
            ],
            options={
                'verbose_name': 'Состояние пользователя',
                'verbose_name_plural': 'Состояния пользователей',
            },
        ),
    ]