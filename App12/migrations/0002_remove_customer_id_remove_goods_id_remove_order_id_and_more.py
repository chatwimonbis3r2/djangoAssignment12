# Generated by Django 4.1.6 on 2023-02-06 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App12', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='customer',
            name='cid',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='surname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='telephone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='goods',
            name='brand',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='goods',
            name='gid',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='goods',
            name='goodsCategory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='App12.goodscategory'),
        ),
        migrations.AddField(
            model_name='goods',
            name='model',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='goods',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='goods',
            name='net',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='goods',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='goodscategory',
            name='gc_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='App12.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='order',
            name='oid',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='App12.order'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]