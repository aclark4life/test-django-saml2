from django.shortcuts import render

# Create your views here.

from idptest.saml2idp.views import _generate_response
from project.app.absorb_lms_sp import Processor

processor = Processor()
processor._request_params = {}

def generate_response(request):
    processor._reset(request)
    return _generate_response(request, processor)
    
