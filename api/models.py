from django.db import models
import os
import time
from datetime import datetime
import pytz


class Cart(models.Model):
    pass


# Create your models here.
class Position(models.Model):
    CATEGORIES = [
        ('FL', 'Цветы'),
        ('DO', 'Веснушки'),
        ('WO', 'Слова'),
        ('AN', 'Животные'),
        ('OT', 'Другое'),
        ('ON', 'Однушки'),
        ('SE', 'Наборы')
    ]
    name = models.CharField(max_length=128, null=False)
    price = models.IntegerField(null=False)
    sale_price = models.IntegerField(null=True, blank=True)
    category=models.CharField(null=False, max_length=2, choices=CATEGORIES)
    image = models.FileField(null=False, upload_to='images/')
    amount = models.IntegerField(null=False, default=0)
    

    def __str__(self) -> str:
        return "<Position>: {}|{} {}".format(
            self.category, 
            self.name, 
            "SALE {}".format(self.sale_price) if self.sale_price else ""
        )
    
    def filename(self):
        return "static/img/"+os.path.basename(self.image.name)

    def to_dict(self) -> str:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "sale_price" : self.sale_price,
            "category": self.category,
            "image": self.filename(),
            "avail_amout": self.amount
        }


class CartPosition(models.Model):
    amount = models.IntegerField(null=False, blank=False)
    cart = models.ForeignKey(Cart, null=True, unique=False, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, unique=False, on_delete=models.CASCADE)

    def __str__(self):
        return "CartPosition: {} x {}".format(self.position.name, self.amount)

    def to_dict(self) -> str: 
        return {
            "amount": self.amount,
            "position": self.position.to_dict()
        }


class Promocode(models.Model):
    code = models.CharField(max_length=128)
    profit_percent = models.IntegerField()
    expiry = models.DateTimeField(default=datetime.fromtimestamp(time.time() + 2592000))
    once = models.BooleanField(default=False)
    used = models.BooleanField(default=False)

    def __str__(self):
        return "Promocode: {}".format(self.code)

    def validate(self):
        utc = pytz
        if self.expiry < datetime.now(self.expiry.tzinfo):
            return (False, 'expiried')

        if self.once and self.used:
            return (False, 'activated')
        
        return (True, 'active')