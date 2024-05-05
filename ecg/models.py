from django.db import models
from django.shortcuts import render


from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks

# Create your models here.


class EcgPage(Page):
    """This page is for ECG project"""

    classification = StreamField(
        [
            ('prediction',blocks.StructBlock(
                [
                    ('label',blocks.ChoiceBlock(choices=[('F','F'),('M','M'),('N','N'),('V','V'),('S','S'),('Q','Q')], help_text="Choose Label")),
                    ('description',blocks.RichTextBlock(features=[ 'bold', 'italic', 'link'], help_text="Some Description"))
                ]
            ))
        ],
        use_json_field=True,
        blank=True,
    )


    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [

            ],
            heading="Form Page Data",
        ),
        MultiFieldPanel(
            [
                FieldPanel('classification')
            ],
            heading="Result Page Data"
        ),
    ]


    def serve(self, request):
        from .forms import UploadECGForm

        if request.method == 'POST':
            """for submission of form in this page"""
            form = UploadECGForm(request.POST, request.FILES)
            if form.is_valid():
                print("Got the image")

                return render(request, 'ecg/ecg_result.html', {
                    'page':self
                    }
                )
            else:
                print("form invalid")

        else:
            form = UploadECGForm()

        return render(request, 'ecg/ecg_page.html', {
            'page':self,
            'form':form
            }
        )
    
