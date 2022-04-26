from django.contrib import admin
from django.urls import path

from crud.views import IndexView,CrudDeleteView

urlpatterns = [
    
    
    path('crud/', IndexView.as_view(),name='home'),
    path('<pk>/delete',CrudDeleteView.as_view(),name='crud_delete')
    ]




