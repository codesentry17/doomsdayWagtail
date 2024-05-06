from django.db import models
from django.shortcuts import render


from wagtail.models import Page, Locale
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks

from .views import predictionFunction
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from pages.models import Blog

# Create your models here.


class EcgPage(Page):
    """This page is for ECG project"""

    subpage_types = ['EcgResult']

    classification = StreamField(
        [
            ('prediction',blocks.StructBlock(
                [
                    ('label',blocks.ChoiceBlock(choices=[('F','F'),('M','M'),('N','N'),('V','V'),('S','S'),('Q','Q')], help_text="Choose Label")),
                    ('description',blocks.RichTextBlock(features=[ 'bold', 'italic', 'link'], help_text="Some Description"))
                ]
            ))
        ],
        max_num=6,
        use_json_field=True,
        blank=True,
    )


    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('classification')
            ],
            heading="Form Page Data"
        ),
    ]


    def serve(self, request):
        from .forms import UploadECGForm

        if request.method == 'POST':
            """for submission of form in this page"""
            form = UploadECGForm(request.POST, request.FILES)
            if form.is_valid():
                print("Got the image")

                mypic1 = form.cleaned_data['mypic1']

                # un-used
                # randomInput = form.cleaned_data['randomInput']

                predicted_label = predictionFunction(mypic1)

                try:
                    page = EcgResult.objects.live().get(label=predicted_label, locale=Locale.get_active())

                    return render(request, 'ecg/ecg_result.html', {
                        'page':page, 
                        'predicted_label':predicted_label
                    })
                    
                except ObjectDoesNotExist:
                    return HttpResponse("This page is not yet created by the admin")

                
            else:
                print("form invalid")

        else:
            form = UploadECGForm()

        return render(request, 'ecg/ecg_page.html', {
            'page':self,
            'form':form
            }
        )
    

class EcgResult(Page):
    """ECG results page, make 6 pages in total"""

    parent_page_types = ['EcgPage']

    label = models.CharField(max_length=1, choices=[
        ('F','F'),
        ('M','M'),
        ('N','N'),
        ('Q','Q'),
        ('S','S'),
        ('V','V')],
        help_text="This is important") 
    
    description = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('label'),
        FieldPanel('description')
    ]




# can refer later to 
# from wagtail.contrib.routable_page.models import RoutablePageMixin, path

# class EcgResult2(RoutablePageMixin, Page):
#     """This page is meant for displaying the ecg upload results"""

#     parent_page_types = ['EcgPage']

#     label = models.CharField(max_length=1, choices=[
#         ('F','F'),
#         ('M','M'),
#         ('N','N'),
#         ('Q','Q'),
#         ('S','S'),
#         ('V','V')],
#         help_text="This is important")
    
#     discription = RichTextField()

#     content_panels = Page.content_panels + [
#         FieldPanel('label'),
#         FieldPanel('discription')
#     ]








