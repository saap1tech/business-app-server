from base_app.views import getFilms, getProducts, getServices
from django.urls import path

urlpatterns = [
    path('films/', getFilms),
    path('services/', getServices),
    path('products/', getProducts)
]
