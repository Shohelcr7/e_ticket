from django.urls import path
from . import views


app_name ='landing'

urlpatterns = [
path('',views.ElectronicVoting.as_view() , name = 'home'),
