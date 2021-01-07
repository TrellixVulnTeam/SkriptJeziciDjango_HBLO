# Generated by Django 3.1.5 on 2021-01-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telefoni', '0003_article_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='marka',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='article',
            name='naziv',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='article',
            name='sistem',
            field=models.CharField(default='', max_length=32),
        ),
    ]
