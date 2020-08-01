
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('add_dojo', views.create_dojo),
    path('add_ninja', views.create_ninja)
    

]
