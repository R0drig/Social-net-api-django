# Generated by Django 3.2.7 on 2021-12-01 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_rename_author_like_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='created_at',
        ),
    ]