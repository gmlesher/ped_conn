# Generated by Django 4.0.5 on 2022-08-07 01:43

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('blog', '0007_remove_blogauthor_social_media_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='caption',
        ),
        migrations.AlterField(
            model_name='blogauthorsorderable',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blog.blogauthor'),
        ),
        migrations.AlterField(
            model_name='blogpagegalleryimage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='blogpagegalleryimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_image', to='blog.blogpage'),
        ),
    ]