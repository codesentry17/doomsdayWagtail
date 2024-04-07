from .models import Navbar
from wagtail.models import Locale

def navbar_request(request):
    
    navbar = Navbar.objects.filter(locale=Locale.get_active()).first()
    
    if navbar is not None:
        return {
            'WebName1':navbar.name1,
            'WebName2':navbar.name2,
            'WebNameOnClick':navbar.redirect,
            'tabs':navbar.nav_tab.all()
        }

    return { }