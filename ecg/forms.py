from django import forms

class UploadECGForm(forms.Form):
    randomInput = forms.CharField(label='Just Testing, enter text here')
    mypic1 = forms.FileField(label='Upload the ECG Graph', widget=forms.ClearableFileInput(attrs={'class': 'link-btn glass'}))