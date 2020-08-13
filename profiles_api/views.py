from rest_framework_views import APIview
from rest_framework_response import Response

class HelloApi(APIview):

    def get(self, request,format=None):
        an_api = ['hello','hey','hiiii','hyeee']

        return Response({'message':"hi","an_api":an_api})
