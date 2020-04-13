

# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.

class Shop(models.Model):
    shopname = models.CharField('店名', max_length=100)
    category = models.CharField('カテゴリ',max_length=20)
    text = models.TextField('説明')
    hours = models.TextField('営業時間')
    closed = models.DateField('定休日')
    address = models.TextField('住所')
    phone = models.CharField('電話番号', max_length=14)