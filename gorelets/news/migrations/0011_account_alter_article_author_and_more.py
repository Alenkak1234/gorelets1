# Generated by Django 4.2.7 on 2024-02-19 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='news.author')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.author'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.category'),
        ),
    ]
