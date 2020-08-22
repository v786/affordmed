from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import MyUserSerializer
# Create your views here.

@api_view(['POST'])
def register(request):
    data = JSONParser().parse(request)
    serializer = MyUserSerializer(data=data)
    if serializer.is_valid():
        serializer.create(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    userData = request.data

@api_view(['POST'])
def updateDetails(request):
    userData = request.data

@api_view(['POST'])
def updatePassword(request):
    userData = request.data