from django.shortcuts import render, HttpResponseRedirect
from .models import contacts
from .forms import ContactSearch
from django.db.models import Q
# Create your views here.


def home(request):
    data = contacts.objects.all()
    diction={ 'data':data}
    return render(request, 'search/index.html', context=diction)

            

def search(request):
    givenSearch = request.GET['search']
    searchResult = contacts.objects.filter(Q(name__icontains=givenSearch ))
    diction={'searchResult':searchResult, 'givenSearch':givenSearch}
    return render(request, 'search/search.html', context=diction)