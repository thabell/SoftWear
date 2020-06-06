# Generated by Django 3.0.5 on 2020-06-06 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_auto_20200605_0127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='refund',
            options={'ordering': ['done', '-date'], 'verbose_name': 'Заявка на возврат', 'verbose_name_plural': 'Заявки на возврат'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['viewed', '-date'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='refund',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refund_item', to='main.Item', verbose_name='Вещь'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refund', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_item', to='main.Item', verbose_name='Вещь'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL),
        ),
    ]
