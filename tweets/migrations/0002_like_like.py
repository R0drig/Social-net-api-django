# Generated by Django 3.2.7 on 2021-12-01 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]