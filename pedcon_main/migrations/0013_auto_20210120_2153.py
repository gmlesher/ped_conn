# Generated by Django 3.1.3 on 2021-01-20 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedcon_main', '0012_auto_20210116_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='practiceinformation',
            old_name='first_name',
            new_name='client_first_name',
        ),
        migrations.RenameField(
            model_name='practiceinformation',
            old_name='last_name',
            new_name='client_last_name',
        ),
    ]