from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from django.views.generic.edit import DeleteView
from crud.models import Details
from django.http import JsonResponse

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['insert_me'] = Details.objects.all()
        return context

class CrudDeleteView(DeleteView):
    model = Details

    def get(self, request, *args, **kwargs):
        # with transaction.atomic():
            try:
                object = self.get_object()
                if object.delete():
                    response = {
                        'success': 'Record has been deleted successfully',
                    }
                else:
                    response = {
                        'error': 'Record could not be deleted',
                    }

            except IntegrityError:
                response = {
                    'error': 'Deleting this Record has been restricted. Please contact your administrator',
                }
            return JsonResponse(response)
