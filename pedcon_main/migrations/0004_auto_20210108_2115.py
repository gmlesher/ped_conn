# Generated by Django 3.1.3 on 2021-01-08 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedcon_main', '0003_auto_20210108_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='practiceinformation',
            old_name='SigdataURL',
            new_name='sig_data_URL',
        ),
    ]
