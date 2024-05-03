from django.db import models
from django.shortcuts import render


from wagtail.models import Page

# Create your models here.


class EcgPage(Page):
    """This page is for ECG project"""

    def serve(self, request):
        from .forms import UploadECGForm

        if request.method == 'POST':
            """for submission of form in this page"""
            form = UploadECGForm(request.POST, request.FILES)
            if form.is_valid():
                print("Got the image")

                return render(request, 'ecg/ecg_result.html', {
                    'context':"These are your results"
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