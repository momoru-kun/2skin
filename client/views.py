#from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.
class Index(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self, request):
        return Response(None, status=status.HTTP_200_OK, template_name='index.html')

#def NotFound(request, exception):
#    return page_not_found(request, exception, template_name='404.html')
