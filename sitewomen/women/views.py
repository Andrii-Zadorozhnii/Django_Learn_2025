from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):
    return render(request, 'women/index.html')

def about(request):
    return render(request, 'women/about.html')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Category</h1><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):

    if request.GET:
        print(request.GET)

    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Category</h1><p>slug: {cat_slug}</p>')

def archive(request, year):

    if year > 2023:
        uri = reverse('cats', args=('sport',))
        return redirect('/')
    return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')