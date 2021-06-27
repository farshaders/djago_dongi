from django.db import models
from django.utils.timezone import now



class user(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.first_name

class buy(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    price = models.FloatField()
    date = models.DateTimeField(default=now)
    def __str__(self):
        return self.product
    def __str__(self):
        return self.price
    def __str__(self):
        return self.date
    def __str__(self):
        return self.user_id


class consumer(models.Model):
    id = models.AutoField(primary_key=True)
    User_id = models.CharField(("consumer"),max_length=50)
    buy_id = models.CharField(max_length=50)
