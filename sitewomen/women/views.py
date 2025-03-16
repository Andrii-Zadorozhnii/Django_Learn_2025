

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = ["About", 'Add post', 'Contact', 'Login']
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b



def index(request):

    data = {
        "title": "main page",
        "menu": menu,
        "float": 28.56,
        "lst": [1, 2, "three", True],
        "set": {1,2,3,4,5},
        "dict": {"key_1": "value_1", "key_2": "value_2"},
        "obj": MyClass(10,20),
    }
    return render(request, 'women/index.html', data)


def about(request):

    data = {"title": "About"}
    return render(request, 'women/about.html', data)




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

