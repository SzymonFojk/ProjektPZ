# Generated by Django 3.1.7 on 2021-04-06 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20210406_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date_list',
            new_name='date_posted',
        ),
    ]
