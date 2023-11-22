from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request=request, template_name='main/home.html')