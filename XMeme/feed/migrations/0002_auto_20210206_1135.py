# Generated by Django 3.1.6 on 2021-02-06 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
