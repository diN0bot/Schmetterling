from django.views.generic.simple import direct_to_template

# Create your views here.

def index(request):
    return direct_to_template(request, 'index.html')
