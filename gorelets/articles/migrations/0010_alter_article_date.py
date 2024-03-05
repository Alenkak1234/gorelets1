# Generated by Django 4.2.7 on 2024-02-26 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Дата публикации'),
        ),
    ]