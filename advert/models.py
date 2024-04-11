from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail import blocks



from wagtail.contrib.forms.models import AbstractForm, AbstractFormField, FORM_FIELD_CHOICES
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel

from wagtail.contrib.forms.forms import FormBuilder
from wagtail.images.fields import WagtailImageField

import json
from os.path import splitext

from django.core.serializers.json import DjangoJSONEncoder

from wagtail.images import get_image_model



from wagtail.contrib.forms.views import SubmissionsListView
from django.utils.html import format_html
from django.urls import reverse

from wagtail.models import Collection



from wagtailcaptcha.models import WagtailCaptchaForm
from wagtailcaptcha.forms import WagtailCaptchaFormBuilder














# doing the ad filling panel

from wagtail.snippets.models import register_snippet


@register_snippet
class Ad(models.Model):

    """Ad Showcasing Model"""

    photo = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title = models.CharField(max_length=30)                         
    description = models.CharField()                   
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    location = models.URLField(blank=True, null=True)

    DAY_CHOICES = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]
    dayF = models.CharField(max_length=3, choices=DAY_CHOICES, blank=True, null=True, verbose_name = 'From')
    dayT = models.CharField(max_length=3, choices=DAY_CHOICES, blank=True, null=True, verbose_name = 'To')
    open_time = models.TimeField(blank=True, null=True)
    close_time = models.TimeField(blank=True, null=True)




    panels = [
        FieldPanel('photo'),

        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('description')
        ],
        heading = 'About Ad'),

        FieldRowPanel(
        [
            FieldPanel('website'),
            FieldPanel('phone'),
            FieldPanel('email')
        ],
        heading = 'Contact Info'),

        FieldPanel('location'),

        FieldRowPanel(
            [
                FieldPanel('dayF'),
                FieldPanel('dayT'),
            ],
            heading = 'Days'
        ),

        FieldRowPanel(
            [
                FieldPanel('open_time'),
                FieldPanel('close_time'),
            ],
            heading="Hours",
        )
    ]


    def __str__(self) -> str:
        return self.title