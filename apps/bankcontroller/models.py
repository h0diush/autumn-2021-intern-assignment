import datetime as dt
import random

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import DecimalValidator
from apps.users.models import User


def price_less_than_one(price):
    if price < 1:
        raise ValidationError('Услуга не может быть бесплатной')


class Wallet(models.Model):
    '''Кошелек'''

    number_walet = models.CharField(
        _("Номер кошелька"), max_length=7, unique=True, null=True, blank=True)
    balance = models.DecimalField(
        _('Баланс'), decimal_places=2, max_digits=10, default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name=_('Пользователь'), related_name='wallets'
    )
    cards = models.ManyToManyField('MoneyCard', verbose_name=_(
        'Денежные карточки'), blank=True, related_name='wallets')

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'

    def __str__(self):
        return f'{self.user} - {self.number_walet}'

    def save(self, *args, **kwargs):
        if not self.number_walet:
            self.number_walet = str(random.randint(100000, 999999))
        super(Wallet, self).save(*args, **kwargs)


class MoneyCard(models.Model):
    '''Денежная карточка'''

    YEARS = [
        (str(year), str(year),)
        for year in range(dt.datetime.now().year, dt.datetime.now().year + 5)
    ]

    MONTH = (
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )

    number = models.CharField(_('Номер карточки'), max_length=16)
    year = models.CharField(
        _('Год'),
        max_length=4,
        choices=YEARS,
        default=dt.datetime.now().year
    )
    month = models.CharField(
        _('Месяц'),
        max_length=8,
        choices=MONTH,
        default=dt.datetime.now().month
    )
    amount = models.DecimalField(_('Сумма'), max_digits=10, decimal_places=2)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name=_('Пользователь'), related_name='moneycards'
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Денежная карточка'
        verbose_name_plural = 'Денежные карточки'

    def __str__(self):
        return (
            f'Зачисление №{self.id} на сумму: {self.amount}. '
            f'Пользователем: {self.user}'
        )


class Service(models.Model):
    '''Услуги'''

    CUREENCY = (
        ('USD', 'USD'),
        ('RUB', 'RUB'),
        ('EUR', 'EUR'),
        ('BYN', 'BYN')
    )

    name = models.CharField(_("Название услуги"), max_length=55)
    description = models.TextField(_('Описание'))
    price = models.DecimalField(
        _('Цена услуги'), max_digits=10, decimal_places=2,
        validators=[
            DecimalValidator(max_digits=10, decimal_places=2),
            price_less_than_one
        ])
    currency = models.CharField(
        _('Валюта'), choices=CUREENCY, default='BYN', max_length=6)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-id']

    def __str__(self):
        return f'{self.name}'

    def validate_price(self, price):
        if price < 1:
            raise ValidationError('Услуга не может юыть бесплатной')
        return price


class ShopService(models.Model):
    '''Покупка услуги'''

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='shops', verbose_name=_('Пользователь')
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE,
        related_name='shop', verbose_name=_('Услуга')
    )
    date = models.DateTimeField(_('Дата покупки'), auto_now_add=True)

    class Meta:
        verbose_name = 'Покупка услуги'
        verbose_name_plural = 'Покупки услуги'
        ordering = ['-date']

    def __str__(self):
        return (
            f"{self.user} купил услугу {self.service.name} "
            f"за {self.service.price}"
        )


class MoneyTransfer(models.Model):

    user_transfer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name=_('Пользователь, который перевел'),
        related_name='money_transfer'
    )
    user_received = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name=_('Пользователь, который получил'),
        related_name='money_recived'
    )
    amount = models.DecimalField(_('Сумма'), max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Перевод денежных средств'
        verbose_name_plural = 'Переводы денежных средств'

    def __str__(self) -> str:
        return (
            f"{self.user_transfer} -> {self.user_received} ({self.amount})"
        )
