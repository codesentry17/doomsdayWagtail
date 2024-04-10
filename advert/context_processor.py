from .models import Ad

def get_ads(request):
    
    ads = Ad.objects.all()
    
    return {
        'ads':ads
    }