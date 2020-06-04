# Generated by Django 3.0.5 on 2020-06-03 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_auto_20200603_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartPiece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='main.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_piece', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Покупка в корзине',
                'verbose_name_plural': 'Покупки в корзине',
            },
        ),
    ]
