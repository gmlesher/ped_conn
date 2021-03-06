# Generated by Django 3.1.3 on 2021-04-09 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedcon_main', '0013_auto_20210120_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='HipaaInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_info', models.CharField(blank=True, max_length=100, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('sig_data_URL', models.TextField(blank=True)),
                ('sig_img', models.ImageField(blank=True, upload_to='sig_images/hipaa_form_sigs')),
                ('filename', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
