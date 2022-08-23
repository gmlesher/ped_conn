from django.db import models
from django import forms
from django.utils.text import slugify

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import StreamField
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


class BlogIndexPage(Page):

    def get_context(self, request, *args, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request, *args, **kwargs)
        blogpages = BlogPage.objects.live().public().order_by('-first_published_at')
        category_slug = request.GET.get('category', None)
        if category_slug:
            context['category_name'] = category_slug.title().replace("-", " ")
            if blogpages.filter(categories__slug=category_slug).count() > 0:
                context['blogpages'] = blogpages.filter(
                    categories__slug=category_slug)
                
        else:
            context['blogpages'] = blogpages
  
        context['category_slug'] = category_slug
        context['authors'] = BlogAuthor.objects.all()
        context['categories'] = BlogCategory.objects.all().order_by('name')

        return context
class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )
class BlogPage(Page):
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('block_quote', blocks.BlockQuoteBlock()),
        ('embed', EmbedBlock()),
    ])
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    authors = ParentalManyToManyField('blog.BlogAuthor', blank=True)

    def main_image(self):
        gallery_item = self.gallery_image.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel(
                'categories', 
                widget=forms.CheckboxSelectMultiple
            ),
        ], heading="Blog information"),
        MultiFieldPanel([
            InlinePanel(
                'blog_authors', 
                label="Author", 
                min_num=1, 
                max_num=2
            )
        ], heading="Authors"),
        InlinePanel('gallery_image', label="Gallery image", max_num=1),
        StreamFieldPanel('body'),
    ]
class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE,
                       related_name='gallery_image')
    image = models.ForeignKey(
        'wagtailimages.Image', 
        on_delete=models.CASCADE, 
        related_name='+',
        null=True,
        blank=True,
    )

    panels = [
        ImageChooserPanel('image'),
    ]
class BlogAuthorsOrderable(Orderable):
    """allows selection of one or more authors for blog post"""

    page = ParentalKey(BlogPage, on_delete=models.CASCADE,
                       related_name='blog_authors')
    author = models.ForeignKey(
        "blog.BlogAuthor",
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True
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
@register_snippet
class BlogAuthor(models.Model):
    """Blog author snippets"""
    name = models.CharField(max_length=100)
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

        ], heading="Name and Image")
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

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        self.slug = slugify(self.name)
    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = 'Blog Categories'
        ordering = ["name"]