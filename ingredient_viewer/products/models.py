from django.db import models


# Create your models here.
class Product(models.Model):
    """
    A class that represents information about a product such as:
        - a name
        - ingredients of the product
    """
    product_name = models.TextField(primary_key=True, help_text='Add product here.')
    ingredients = models.TextField(help_text='Add ingredients here.')
    image = models.ImageField(blank=False, help_text='Add an image for the product.')

    def __str__(self):
        return '{}'.format(self.product_name)