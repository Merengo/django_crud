from django.contrib import admin
from django.urls import path

from crud.views import IndexView,CrudDeleteView,ListView,CrudCreateView,CrudUpdateView

urlpatterns = [
    
    
    path('list/', ListView.as_view(),name='home'),
    path('<pk>/delete',CrudDeleteView.as_view(),name='crud_delete'),
    path('create',CrudCreateView.as_view(),name='crud_create'),
    path('<pk>/edit',CrudUpdateView.as_view(),name='crud_update'),
    ]




