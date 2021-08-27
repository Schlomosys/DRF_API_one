from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView

from .models import Category, Organisation
from .serializers import CategorySerializer, OrganisationSerializer, QRSerializer, QRtestSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny


from .generator import generate_qr

#DECORATORS+++++++++++++++++++++++++++++++++++++++++++++++++
from rest_framework.response import Response
from rest_framework.views import status



def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        text = args[0].request.data.get("text", None)
        if not text:
            return Response(
                data={
                    "message": "Text is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated

class CreateQRView(CreateAPIView):
    """
    POST create/
    """
    #permission_classes = (permissions.AllowAny,)
    #permission_classes = (IsAuthenticated,)
    queryset = ''
    serializer_class = QRtestSerializer
    #throttle_classes = [AnonRateThrottle]

    @validate_request_data
    def create(self, request, *args, **kwargs):
        text = request.data['text']
        
        output = generate_qr(text)
        #result = QRSerializer(output).data
        return Response(
            data=output,
            status=status.HTTP_201_CREATED
        )
        

class CategoryListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryCreateAPIView(CreateAPIView):
    """
    API view to retrieve list of posts or create new
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (AllowAny)
    def create(self, request, *args, **kwargs):
        
        owner = request.data['owner']
        name= request.data['name']
        description = request.data['description']
        logo=request.data['logo']
        category= Category(owner=owner, name=name, description=description, logo=logo)
        category.save()


        return Response(
            data="Categorie creer avec success",
            status=status.HTTP_201_CREATED
        )
class CategoryListAPIView(ListAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
       

    
    

class CategoryDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class OrganisationListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()


class OrganisationDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()
