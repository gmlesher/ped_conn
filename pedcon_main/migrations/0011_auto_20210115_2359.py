# Generated by Django 3.1.3 on 2021-01-15 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedcon_main', '0010_auto_20210115_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='safeandsoundinformation',
            name='completed_ssp',
        ),
        migrations.RemoveField(
            model_name='safeandsoundinformation',
            name='completed_ssp_comm',
        ),
        migrations.RemoveField(
            model_name='safeandsoundinformation',
            name='gs_comm',
        ),
        migrations.RemoveField(
            model_name='safeandsoundinformation',
            name='parent_first_name',
        ),
        migrations.RemoveField(
            model_name='safeandsoundinformation',
            name='parent_last_name',
        ),
        migrations.AddField(
            model_name='safeandsoundinformation',
            name='form_completed_by',
            field=models.CharField(choices=[('', ''), ('Parent', 'Parent'), ('Self', 'Self')], default='abc', max_length=100),
        ),
        migrations.AddField(
            model_name='safeandsoundinformation',
            name='pre_or_post',
            field=models.CharField(choices=[('', ''), ('Pre-treatment', 'Pre-treatment'), ('Post-treatment', 'Post-treatment')], default='abc', max_length=100),
        ),
        migrations.AlterField(
            model_name='safeandsoundinformation',
            name='ss_comm',
            field=models.TextField(blank=True, null=True, verbose_name='Comments'),
        ),
    ]
