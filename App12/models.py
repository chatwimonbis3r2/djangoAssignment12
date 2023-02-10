from django.db import models


# Create your models here.
class GoodsCategory(models.Model):
    gc_name = models.CharField(max_length=100, default='')
    desc = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.id) + ' : ' + str(self.gc_name)


class Goods(models.Model):
    goodsCategory = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, default=None)
    gid = models.CharField(max_length=10, default='', primary_key=True)
    name = models.CharField(max_length=100, default='')
    brand = models.CharField(max_length=100, default='')
    model = models.CharField(max_length=100, default='')
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    property = models.TextField(default='')

    def __str__(self):
        return str(self.goodsCategory) + ' : ' + self.gid + ' : ' + self.name


class Customer(models.Model):
    cid = models.CharField(max_length=10, default='', primary_key=True)
    name = models.CharField(max_length=100, default='')
    surname = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    address = models.TextField(default='')
    telephone = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=20, default='')
    carreer = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.cid + ' : ' + self.name


class Order(models.Model):
    oid = models.CharField(max_length=10, default='', primary_key=True)
    date = models.DateField(default=None)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    status = models.CharField(max_length=20, default='')


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    price = models.FloatField(default=0.00)
    quantity = models.IntegerField(default=0)
