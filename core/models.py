from django.db import models

class Product (models.Model):
    pro_name = models.CharField('Nome', max_length=100)
    pro_price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    pro_stock = models.IntegerField('Quantidade em Estoque')


    def __str__(self):
        return self.name