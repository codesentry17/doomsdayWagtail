 # Create your models here.
from django.db import models
# Create your models here.

from wagtail.snippets.models import register_snippet
from wagtail.models import TranslatableMixin

from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel, FieldRowPanel
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail import blocks






class NavTab(Orderable):
    """the navbar tabs, consist of multiple pages"""

    navbar = ParentalKey('Navbar', related_name='nav_tab')

    nav_title = models.CharField(max_length=20, blank=True, null=True, help_text="Ignore if single page / external link")

    nav_links = StreamField(
        [
            ('Website_Page', blocks.PageChooserBlock()),
            ('External_Link', blocks.StructBlock(
                [
                    ('Title', blocks.CharBlock()),
                    ('URL', blocks.URLBlock())
                ]
            ))   
        ],
        collapsed = True,
        use_json_field=True,
    )


    panels = [
        FieldPanel('nav_title'),
        FieldPanel('nav_links')
    ]

    @property
    def is_dropdown(self):
        return len(self.nav_links) > 1

    @property
    def routes(self):
        page_urls = set()

        for component in self.nav_links:
            if component.block.name == "Website_Page":
               page_urls.add(component.value.url)

        return page_urls        

    def save(self, **kwargs):

        if not self.nav_title:
            if self.nav_links[0].block.name == "Website_Page":
                self.nav_title = self.nav_links[0].value.title
            else:
                self.nav_title = self.nav_links[0].value.get('Title')

        super(NavTab,self).save(**kwargs)

    def __str__(self) -> str:
        return self.nav_title
    



@register_snippet
class Navbar(ClusterableModel, TranslatableMixin):
    """the navbar that holds NavTabs"""

    name1 = models.CharField(max_length=15, blank=True, null=True)
    name2 = models.CharField(max_length=15)
    redirect = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldRowPanel(
            [
                FieldPanel('name1'),
                FieldPanel('name2'),
                PageChooserPanel('redirect')
            ],
            heading="WebSite Name",
        ),
        InlinePanel('nav_tab', label='Nav Item')
    ]

    class Meta:
        unique_together = ('translation_key', 'locale')

    def __str__(self) -> str:
        return 'Navbar'