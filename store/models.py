from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author = models.CharField(max_length=255)

    def __str__(self):
        return f'ID {self.id}: {self.name}'
