# Generated by Django 3.0.5 on 2020-06-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200602_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cost',
            field=models.FloatField(default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
