from django.shortcuts import render

# Create your views here.
API_KEY = '4fce03da4e834c67a277777ae74631f5'
import requests
from django.http import HttpResponse
from django.views.decorators.cache import never_cache  # Import never_cache decorator


@never_cache  # Decorate your view function with never_cache
def index(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles': articles}

    response = render(request, 'index.html', context)
    
    # Set cache control headers to prevent caching
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response




def category(request,name):
    # url = f'https://newsapi.org/v2/top-headlines?category={name}&apiKey={API_KEY}'
    url = f'https://newsapi.org/v2/top-headlines?country=in&category={name}&apiKey={API_KEY}'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles,'category':name}
    return render(request,'category.html',context)

def search(request):
    search_term = request.GET['search']
    url = f'https://newsapi.org/v2/everything?q={search_term}&apiKey={API_KEY}'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles,'search':search_term}
    return render(request,'search.html',context)


