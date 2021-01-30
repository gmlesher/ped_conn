from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
import datetime


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

choices = Category.objects.all().values_list('name','name')

choice_list = []

# for item in choices:
#     choice_list.append(item)


class Post(models.Model):
    # time-stamp of when blog post was created
    date_created    = models.DateField(auto_now_add=True)

    # all other information necessary for blog post
    title           = models.CharField(max_length=255)
    author          = models.ForeignKey(User, on_delete=models.CASCADE)
    date            = models.DateField(default=datetime.date.today)
    post_image      = models.ImageField(blank=True, null=True, upload_to='images/')
    category        = models.CharField(max_length=255, default="uncategorized", choices=choice_list)
    slug            = models.SlugField()
    body            = RichTextField()

    
    # Post page displays title of post and author divided by "|"
    def __str__(self):
        return self.title + ' | ' + str(self.author.first_name) + ' ' + str(self.author.last_name)

    # slug field is saved as slug from category field on new posts, not old ones
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.category)

        super(Post, self).save(*args, **kwargs)
