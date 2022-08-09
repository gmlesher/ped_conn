# Generated by Django 3.1.3 on 2021-01-20 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210118_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Education', 'Education'), ('About Us', 'About Us'), ('Self Care', 'Self Care')], default='uncategorized', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(),
        ),
    ]
