# Generated by Django 4.2.7 on 2024-02-26 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.RemoveField(
            model_name='article',
            name='like',
        ),
    ]
