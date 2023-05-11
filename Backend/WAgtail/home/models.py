from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    template = 'home/home_page.html'
    blog_title = models.CharField(max_length=100, blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel("blog_title"),
    ]
