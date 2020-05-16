from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View """

    def get(self, request, format=None):
        """returns a list of APIView featues"""
        an_apiview = [
            'Uses HHTP methods as function (get,post,patch,put,delete)'
            'It is similar to a traditional Django View'
            'Gives you the ost control over you '
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
