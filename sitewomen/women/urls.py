from sqlite3 import register_converter

from django.urls import path,re_path

from django.urls import path, register_converter
from . import views
from . import converters

# Регистрируем конвертер
register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='addpage'),
    path('contact/', views.contacts, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),




    # path('cats/<int:cat_id>/', views.categories, name = "cats_id"),
    # path('cats/<slug:cat_slug>/', views.categories_by_slug, name = "cats"),
    # path("archive/<year4:year>/", views.archive, name = "archive"),
]

