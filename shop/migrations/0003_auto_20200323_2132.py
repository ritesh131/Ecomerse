# Generated by Django 3.0.3 on 2020-03-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200323_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='', upload_to='shop/images/productimages'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='', upload_to='shop/images/productimages'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='', upload_to='shop/images/productimages'),
        ),
    ]
