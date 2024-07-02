from django.db import models


class Product (models.Model):
    # CharField is short for character field. It represents a field that can contain text. You can use this to prevent a hacker from storing information with an enormously large name which could break your app.
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    # 2083 is the standard maximum length for characters
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()





