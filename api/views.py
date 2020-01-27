from django.http import HttpResponse
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from . models import users
from .serializers import usersSerializer

# Just wraps a simple HTTP Response to a JSON Response
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)

def index(request):
    return HttpResponse("&lt;h3&gt;Welcome to User API v1.0&lt;/h3&gt;")

@api_view(['GET'])
def users(request):
    users = users.objects.all()
    serializer = usersSerializer(users, many=True)
    return JSONResponse(serializer.data)
