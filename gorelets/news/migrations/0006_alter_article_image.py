# Generated by Django 4.2.7 on 2024-02-13 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default image', upload_to='images/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]