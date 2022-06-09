from django.db import models
from django import forms

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.search import index
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase

from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
import datetime


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request, *args, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request, *args, **kwargs)
        blogpages = BlogPage.objects.live().public().order_by('-first_published_at')
        category_slug = request.GET.get('category', None)
        if category_slug:
            if blogpages.filter(categories__slug=category_slug).count() > 0:
                context['blogpages'] = blogpages.filter(
                    categories__slug=category_slug)
        else:
            context['blogpages'] = blogpages

        context['category_slug'] = category_slug
        context['authors'] = BlogAuthor.objects.all()
        context['categories'] = BlogCategory.objects.all().order_by('name')

        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('raw_HTML', blocks.RawHTMLBlock()),
        ('block_quote', blocks.BlockQuoteBlock()),
        ('embed', EmbedBlock()),
    ])
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    authors = ParentalManyToManyField('blog.BlogAuthor', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        MultiFieldPanel([
            InlinePanel('blog_authors', label="Author", min_num=1, max_num=4)
        ], heading="Authors"),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE,
                       related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class BlogAuthorsOrderable(Orderable):
    """allows selection of one or more authors for blog post"""

    page = ParentalKey(BlogPage, on_delete=models.CASCADE,
                       related_name='blog_authors')
    author = models.ForeignKey(
        "blog.BlogAuthor",
        on_delete=models.CASCADE,
        related_name='+',
    )

    panels = [
        SnippetChooserPanel("author"),
    ]


class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blog_index'] = BlogIndexPage.objects.first()
        context['blogpages'] = blogpages
        return context


class WebsiteBlock(blocks.StructBlock):
    website_name = blocks.CharBlock()
    website_link = blocks.URLBlock()


class SocialMediaBlock(blocks.StructBlock):
    social_media_name = blocks.CharBlock()
    social_media_link = blocks.URLBlock()


@register_snippet
class BlogAuthor(models.Model):
    """Blog author snippets"""
    name = models.CharField(max_length=100)
    website = StreamField([
        ('website_block', WebsiteBlock(max_num=1)),
    ], blank=True, null=True)
    social_media = StreamField([
        ('social_media_block', SocialMediaBlock()),
    ], blank=True, null=True, verbose_name="Social Media & Other")
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("name"),
            ImageChooserPanel("image"),

        ], heading="Name and Image"),
        MultiFieldPanel([
            StreamFieldPanel("website"),
            StreamFieldPanel("social_media"),
        ], heading="Links"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Author"
        verbose_name_plural = 'Blog Authors'
        ordering = ["name"]


@register_snippet
class BlogCategory(models.Model):
    """Blog category snippets"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text="A slug to identify posts by this category",
    )
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = 'Blog Categories'
        ordering = ["name"]


# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


# choices = Category.objects.all().values_list('name', 'name')

# choice_list = []

# for item in choices:
#     choice_list.append(item)


# class Post(models.Model):
#     # time-stamp of when blog post was created
#     date_created = models.DateField(auto_now_add=True)

#     # all other information necessary for blog post
#     title = models.CharField(max_length=255)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField(default=datetime.date.today)
#     post_image = models.ImageField(blank=True, null=True, upload_to='images/')
#     category = models.CharField(
#         max_length=255, default="uncategorized", choices=choice_list)
#     slug = models.SlugField()
#     body = RichTextField()

#     # Post page displays title of post and author divided by "|"

#     def __str__(self):
#         return self.title + ' | ' + str(self.author.first_name) + ' ' + str(self.author.last_name)

#     # slug field is saved as slug from category field on new posts, not old ones
#     def save(self, *args, **kwargs):
#         if not self.id:
#             # Newly created object, so set slug
#             self.slug = slugify(self.category)

#         super(Post, self).save(*args, **kwargs)
