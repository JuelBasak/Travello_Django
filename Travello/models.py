from django.db import models

# Create your models here.
class Destination(models.Model):

    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    # def __init__(self, id = 000, name = 'No Data', img = 'No Data', desc = 'No Data', price = 0, offer = False):
    #     self.id = id
    #     self.name = name
    #     self.img = img
    #     self.desc = desc
    #     self.price = price
    #     self.offer = offer
