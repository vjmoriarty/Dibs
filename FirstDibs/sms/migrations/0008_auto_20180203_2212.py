# Generated by Django 2.0.2 on 2018-02-03 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0007_auto_20180203_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dib',
            old_name='image',
            new_name='image_file',
        ),
    ]
