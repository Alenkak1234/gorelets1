# Generated by Django 4.2.7 on 2024-02-19 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_author_article_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AddField(
            model_name='article',
            name='category_id',
            field=models.ForeignKey(choices=[('Поездки', 'Поездки')], null=True, on_delete=django.db.models.deletion.CASCADE, to='news.category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(choices=[('Alyona', 'Alyona')], null=True, on_delete=django.db.models.deletion.CASCADE, to='news.author'),
        ),
    ]
