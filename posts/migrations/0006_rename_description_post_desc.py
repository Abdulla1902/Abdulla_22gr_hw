# Generated by Django 4.1.3 on 2022-12-05 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_hashtag_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='desc',
        ),
    ]