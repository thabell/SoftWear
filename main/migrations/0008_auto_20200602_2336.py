# Generated by Django 3.0.5 on 2020-06-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_item_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cost_fractional',
            field=models.IntegerField(default=0, max_length=2, verbose_name='Цена, коп.'),
        ),
    ]
