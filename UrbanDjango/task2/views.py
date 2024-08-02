from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def vision_func(request):
    return render(request, 'func_view.html' )

class VisionClass(TemplateView):
    template_name='class_view.html'