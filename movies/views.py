from django.shortcuts import render
from .models import *
from user.models import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def movies(request, id):
    profile = Profiles.objects.get(id = id)
    profiller = Profiles.objects.filter(owner = request.user)
    filmler = Movie.objects.all()
    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')
        # filmler = Movie.objects.filter(isim__icontains = search)
        filmler = Movie.objects.filter(
            Q(isim__icontains = search) |
            Q(kategori__isim__icontains = search)
        )
    
    context = {
        'filmler': filmler,
        'profile':profile,
        'profiller': profiller
    }
    return render(request, 'browse-index.html', context)

def search(request):
    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')
        # filmler = Movie.objects.filter(isim__icontains = search)
        filmler = Movie.objects.filter(
            Q(isim__icontains = search) |
            Q(kategori__isim__icontains = search)
        )
    
    context = {
        'filmler': filmler,
        'search': search
    }
    return render(request, 'search.html', context)