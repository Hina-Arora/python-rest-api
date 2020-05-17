from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profile_api import permissions
from profile_api import serializers
from profile_api import models



class HelloApiView(APIView):
    """ Test API View """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of APIView featues"""
        an_apiview = [
            'Uses HHTP methods as function (get,post,patch,put,delete)'
            'It is similar to a traditional Django View'
            'Gives you the ost control over you '
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST )


    def put(self, request, pk=None):
        """Handle updating object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle partial updating object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Handle partial updating object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API view set"""

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""

        a_viewsets = [
            'Uses actions {list , create, retrieve, update, partial_update , remove}'
            'Automatically maps to URLs using routers'
            'Provides more functionality with less code'
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewsets})


    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request, pk=None):
        """hndle getting object by id"""
        return Response({'http_method':'retrieve'})


    def update(self, request, pk=None):
        """handle updating the object"""
        return Response({'http_method':'UPDATE'})

    def partial_update(self, request, pk=None):
        """handle partial updating the object"""
        return Response({'http_method':'PARTIAL UPDATE'})

    def destroy(self, request, pk=None):
        """handle destroy the object"""
        return Response({'http_method':'DESTROY'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handling creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authetication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
