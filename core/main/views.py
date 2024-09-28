"""
This file have to be deleted after frontend and backend connection is succeded
"""
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def hello_world(request):
    if request.method == 'GET':
       return Response({'greeting':"Hello, World!"})