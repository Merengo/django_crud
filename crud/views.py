from django.shortcuts import render,redirect
from django.views.generic import View, TemplateView, ListView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from crud.models import Details

from django.db import IntegrityError
from . import forms
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import DetailsSerializer
# Create your views here.

# the liat view
class ListView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self,**kwargs):
        context = super(ListView,self).get_context_data(**kwargs)
        context['insert_me'] = Details.objects.all()
        return context

# crud deleteview
# class CrudDeleteView(DeleteView):
#     model = Details

#     def get(self, request, *args, **kwargs):
#         # with transaction.atomic():
#             try:
#                 object = self.get_object()
#                 if object.delete():
#                     response = {
#                         'success': 'Record has been deleted successfully',
#                     }
#                 else:
#                     response = {
#                         'error': 'Record could not be deleted',
#                     }

#             except IntegrityError:
#                 response = {
#                     'error': 'Deleting this Record has been restricted. Please contact your administrator',
#                 }
#             return JsonResponse(response)

class CrudDeleteView(DeleteView):
    model = Details

    def get(self, request, *args, **kwargs):
        # with transaction.atomic():
            try:
                object = self.get_object()
                if object.delete():
                   return redirect('crudz:home')
                else:
                    return redirect('crudz:home')

            except IntegrityError:
                response = {
                    'error': 'Deleting this Record has been restricted. Please contact your administrator',
                }
            return JsonResponse(response)


# template view
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['insert_me'] = Details.objects.all()
        return context

# the create view
class CrudCreateView(CreateView):
    form_class = forms.CrudCreateForm
    template_name = 'add.html'

    def form_valid(self, form):
        b = form.save(commit=False)
        b.createhostpc = self.request.META.get('COMPUTERNAME')
        b.userid = self.request.user
        b.save()

        if b:
            return redirect('/crud/list')
        else:
            """If the form is invalid, render the invalid form."""
            return self.render_to_response(self.get_context_data(form=form))
        
    def form_invalid(self, form):
        return self.form_invalid(form=form)

# update view
class CrudUpdateView(UpdateView):
    model = Details
    form_class = forms.CrudUpdateForm
    template_name = 'edit.html'

    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('/crud/list')



# 
class DetailsViewSet(viewsets.ModelViewSet):
    serializer_class = DetailsSerializer
    queryset = Details.objects.all()

