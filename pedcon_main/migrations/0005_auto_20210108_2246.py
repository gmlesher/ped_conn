# Generated by Django 3.1.3 on 2021-01-08 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedcon_main', '0004_auto_20210108_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='practiceinformation',
            name='sig_img',
            field=models.ImageField(blank=True, upload_to='sig_images/'),
        ),
        migrations.AlterField(
            model_name='practiceinformation',
            name='sig_data_URL',
            field=models.TextField(blank=True),
        ),
    ]