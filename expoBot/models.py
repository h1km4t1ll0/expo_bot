from django.db import models


class BotUser(models.Model):
    telegram_id = models.BigIntegerField(
        primary_key=True,
        verbose_name='ID в телеграм',
        null=False,
        blank=False,
    )

    nickname = models.TextField(
        verbose_name='Никнейм',
        null=False,
        blank=False,
    )

    api_hash = models.TextField(
        verbose_name='Хеш для клиента ТГ',
        null=True,
        blank=False,
    )

    api_id = models.TextField(
        verbose_name='API ID для клиента ТГ',
        null=True,
        blank=False,
    )

    phone_number = models.TextField(
        verbose_name='Номер телефона',
        null=True,
        blank=False,
    )

    completed = models.BooleanField(
        default=False,
    )

    # phone_number_hash = models.TextField(
    #     null=True,
    #     blank=True,
    # )

    objects = models.Manager()

    def __str__(self):
        return f'@{self.nickname}'

    class Meta:
        verbose_name = 'Пользователь бота'
        verbose_name_plural = 'Пользователи бота'


class BotUserCondition(models.Model):
    user = models.OneToOneField(
        to=BotUser,
        on_delete=models.CASCADE,
    )

    on_api_hash_input = models.BooleanField(
        verbose_name='Ввод АПИ хеша',
        default=False,
        null=True,
        blank=False,
    )

    on_api_id_input = models.BooleanField(
        verbose_name='Ввод ID АПИ',
        default=False,
        null=True,
        blank=False,
    )

    on_phone_number_input = models.BooleanField(
        verbose_name='Ввод номера телефона',
        default=False,
        null=True,
        blank=False,
    )

    # on_telegram_code_confirmation = models.BooleanField(
    #     verbose_name='Ввод кода телеграм',
    #     default=False,
    #     null=True,
    #     blank=False,
    # )

    # on_code_input = models.BooleanField(
    #     verbose_name='Ввод кода от телеграм',
    #     default=False,
    #     null=True,
    #     blank=False,
    # )

    def __str__(self):
        return f'Состояние для @{self.user.nickname}'

    class Meta:
        verbose_name = 'Состояние пользователя'
        verbose_name_plural = 'Состояния пользователей'


class Bot(models.Model):
    entity = models.TextField(
        verbose_name='ID бота',
        null=True,
        blank=False,
    )
