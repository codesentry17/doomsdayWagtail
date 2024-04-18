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
            

        else:
            form = UploadECGForm()

        return render(request, 'ecg/ecg_result.html', {
            'page':self,
            'form':form
        })