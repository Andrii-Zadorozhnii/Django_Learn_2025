

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

menu= [
    {"title": "About", "url_name": "about"},
    {"title": "Add post", "url_name": "addpage"},
    {"title": "Contact", "url_name": "contact"},
    {"title": "Login", "url_name": "login"},
]

data_db = [
    {"id": 1, "title": "Angelina Joly", "content": "Biography Angelina Joly", "is_published": True},
    {"id": 2, "title": "Meryl Streep", "content": "Biography Meryl Streep", "is_published": False},
    {"id": 3, "title": "Cate Blanchett", "content": "Biography Cate Blanchett", "is_published": True},
    {"id": 4, "title": "Scarlett Johansson", "content": "Biography Scarlett Johansson", "is_published": True},
    {"id": 5, "title": "Natalie Portman", "content": "Biography Natalie Portman", "is_published": False},
    {"id": 6, "title": "Emma Stone", "content": "Biography Emma Stone", "is_published": True},
]


def index(request):

    data = {
        "title": "Main page",
        "menu": menu,
        "posts": data_db,

        # "float": 28.56,
        # "lst": [1, 2, "three", True],
        # "set": {1,2,3,4,5},
        # "dict": {"key_1": "value_1", "key_2": "value_2"},
        # # "obj": MyClass(10,20),
    }
    return render(request, 'women/index.html', data)


def about(request):

    data = {"title": "About"}
    return render(request, 'women/about.html', data)


def show_post(request, post_id):
    return HttpResponse(f'Post id: {post_id}')

def addpage(request):
    return HttpResponse('Add page')

def contacts(request):
    return HttpResponse('Contacts')

def login(request):
    return HttpResponse('Login')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

# def categories(request, cat_id):
#     return HttpResponse(f'<h1>Category</h1><p>id: {cat_id}</p>')

# def categories_by_slug(request, cat_slug):
#
#     if request.GET:
#         print(request.GET)
#
#     if request.POST:
#         print(request.POST)
#     return HttpResponse(f'<h1>Category</h1><p>slug: {cat_slug}</p>')
#
# def archive(request, year):
#
#     if year > 2023:
#         uri = reverse('cats', args=('sport',))
#         return redirect('/')
#     return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')