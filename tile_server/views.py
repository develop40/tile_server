import pdb

from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
import mapnik
from . import utils


class MyView(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        # pdb.set_trace()
        service= self.kwargs['service']
        z= float(self.kwargs['z'])
        x=self.kwargs['x']
        y=self.kwargs['y']
        output = utils.tms(z, x, y, service)
        return HttpResponse(bytes(output), content_type="image/png")



def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# http://localhost:8000/myview/xyz/1.0.0/land/3/2/2.png