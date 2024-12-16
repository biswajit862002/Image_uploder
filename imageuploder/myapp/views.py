from django.shortcuts import render, HttpResponseRedirect
from .models import Image
from .forms import ImageForm

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ImageForm()
    img = Image.objects.all()
    context = {'form':form, 'img':img}
    return render(request, 'myapp/home.html', context)