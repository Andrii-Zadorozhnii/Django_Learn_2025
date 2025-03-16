from sqlite3 import register_converter

from django.urls import path,re_path

from django.urls import path, register_converter
from . import views
from . import converters

# Регистрируем конвертер
register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
    path("archive/<year4:year>/", views.archive),
]