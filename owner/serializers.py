from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Organisation, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


#class UserSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = User
        #fields = ('id', 'username','email', 'first_name', 'last_name',)


class CategorySerializer(serializers.ModelSerializer):
    #tags = TagSerializer(many=True, required=False, read_only=True)
    #author = UserSerializer(required=False, read_only=True)
    serializers.ImageField(use_url=True, required=False, allow_null=True)
   # image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Category
        fields = ('id', 'owner', 'name', 'description', 'logo', ) 

    #defget_image_url(self, obj):
        #return obj.logo.url    
           


class OrganisationSerializer(serializers.ModelSerializer):
    
    #category = CategorySerializer(required=False, read_only=True)
    serializers.ImageField(use_url=True, required=False, allow_null=True)
    

    class Meta:
        model = Organisation
        fields = ('id', 'owner', 'name', 'description', 'logo', 'category',)  
    
  
                  


class QRtestSerializer(serializers.Serializer):
    """
    This serializer is the input to create qr code
    """
    text = serializers.CharField(max_length=200)
class QRSerializer(serializers.Serializer):
    """
    This serializer is the output of create qr code
    """
    file_type = serializers.CharField(max_length=5)
    image_base64 = serializers.CharField(max_length=300)                  