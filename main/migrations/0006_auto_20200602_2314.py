# Generated by Django 3.0.5 on 2020-06-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200602_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cost_fractional',
            field=models.IntegerField(default=0, verbose_name='Цена, коп.'),
        ),
        migrations.AddField(
            model_name='item',
            name='cost_int',
            field=models.IntegerField(default=0, verbose_name='Цена, руб.'),
            preserve_default=False,
        ),
    ]
