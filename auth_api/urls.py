from auth_api.views import signIn, signUp
from django.urls import path

urlpatterns = [
    path("signIn/", signIn),
    path("signUp/", signUp)
]
