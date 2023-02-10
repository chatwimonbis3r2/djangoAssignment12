from django.db import models

class Employee(models.Model):
    empid = models.CharField(max_length=13, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    address = models.TextField(max_length=200, default="")
    status = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=50, default="")
    salary = models.FloatField(default=0.00)
    gender = models.CharField(max_length=10, default="")
    birthday = models.DateField(default=None)
    born = models.CharField(max_length=30)
    marries = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ":" + self.name + "(" + self.status + ")"