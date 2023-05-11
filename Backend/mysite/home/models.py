from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.admin.panels import MultipleChooserPanel

class HomePage(Page):
    templates = 'home/home_page.html'
    blog_title = models.CharField(max_length=100, blank=False, null=True)
    blog_subttle = RichTextField(features = ["bold", "italic"])
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    blog_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )


    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        FieldPanel('blog_subtitle'),
        MultipleChooserPanel(
        'images', label = 'Images', chooser_field_name="image"
        )

    ]

    class Meta:
        verbose_name = "Primary Home Page"
        verbose_name_plural = "Main Home PAge"