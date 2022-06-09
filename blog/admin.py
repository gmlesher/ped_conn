from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple


class Checkbox(admin.ModelAdmin):
    # makes slug field auto-populate with category name
    prepopulated_fields = {'slug': ('category',), }
    # if any m2m fields, all m2m fields are checkboxes instead of list
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},

    }

# admin.site.register(Post, Checkbox)
# admin.site.register(Category)
