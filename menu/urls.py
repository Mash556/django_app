from django.urls import path
from .views import my_view

urlpatterns = [
    path('<str:menu_name>', my_view, name='my_view'),
    path('', my_view, name='my_view_default'),
]
