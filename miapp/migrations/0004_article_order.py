# Generated by Django 3.2.7 on 2021-12-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_auto_20211219_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Orden'),
        ),
    ]
