from django.urls import path
from . import views

# a view called post_list to the root url('')
urlpatterns = [
    path('', views.post_list, name='post_list'),
]