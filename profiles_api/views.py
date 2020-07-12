from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        # return a dictionary or list, which the Response then turns to json
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data) # standard way to retrieve serializer class

        if serializer.is_valid():
            name = serializer.validated_data.get('name') # retrives name we defined in serializer, can retrive anything like this
            message = f'Hello {name}' # returns the string output to say Hello 'name'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors, # will return errors specific to seralizer
            status=status.HTTP_400_BAD_REQUEST # will return the HTTP error code
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        # HTTP put often used to update an object, typically do it to URL primary key (pk)
        # replaces object, with what we provide
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of a knowledge"""
        # typically use this to update specific fields, for example, if change last name but not first, will only change last name
        # updates on fields provided in the request
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        # use this to delete and object in the database
        return Response({'method': 'DELETE'})
