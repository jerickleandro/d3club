from django.urls import path


from .views import index
from .views import contato



urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
]