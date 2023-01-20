from django.shortcuts import render
from . models import place
from . models import animal
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obje=animal.objects.all()

    return render(request,"index.html",{'result':obj,'res':obje})
