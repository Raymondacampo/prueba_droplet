from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "prueba_app/index.html")

def about_us(request):
    return render(request, "prueba_app/about_us.html")