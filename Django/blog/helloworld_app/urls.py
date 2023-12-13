from django.urls import path
from .views import helloworldfunc

urlpatterns = [
    path('helloworld_app/', helloworldfunc)
]