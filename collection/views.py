from django.shortcuts import render
from collection.models import Thing

# Create your views here.
def index(request):
    things = Thing.objects.all()
    #things = Thing.objects.filter(name__contains='Hello')
    return render(request, 'index.html', { 
        'things': things,
        })

def thing_detail(request, slug_template):
    # grab the object
    thing = Thing.objects.get(slug=slug_template)
    # and pass it on to the template
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
        })
