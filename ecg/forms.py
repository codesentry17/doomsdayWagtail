from django import forms

class UploadECGForm(forms.Form):
    mypic1 = forms.FileField(label='Upload the ECG Graph', widget=forms.ClearableFileInput(attrs={'class': 'link-btn glass'}))