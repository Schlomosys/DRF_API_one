from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.views import status


from django.core import serializers

from owner.models import Category, Organisation


class QrcodeGenerateAPIView(APITestCase):
    def setUp(self) ->None:
        self.url =reverse('api-qr-create', kwargs={'version': 'v1'})
    def test_create_category(self):
        data={
            'text':'www.google.com',
        }
        
        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        response_json = response.json()
        print(response_json)



class CategoryCreateAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('api-category-list', kwargs={'version': 'v1'})

    def test_create_category(self):
        self.assertEquals(
            Category.objects.count(),
            0
        )
        data = {
            
            'owner':'owner', 
            'name':'catone',
            'description':'description',  
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Category.objects.count(),
            1
        )
        category = Category.objects.first()
        self.assertEquals(
            category.name,
            data['name']
        )
        self.assertEquals(
            category.owner,
            data['owner']
        )

    def test_get_category_list(self):
        #tag = Tag(name='tag_name')
        #tag.save()
        category = Category(owner='proprio', name='cat', description='descript')
        category.save()
        #post.tags.add(tag)
        category1 = Category(owner='love', name='luv', description='descript')
        category1.save()
        response = self.client.get(self.url, format='json')
        response_json = response.json()
        

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        print(response_json)
        self.assertEquals(
            len(response_json),
            4
        )
        data = response_json['results'][0]
        #data1 = response_json['results'][1]
        #data2 = response_json['results'][2]
        #data3 = response_json['results'][3]
        #print(data)
       # print(data1)
        #print(data2)
        #print(data3)
        self.assertEquals(
            category.name,
            data['name']
        )
        self.assertEquals(
            category.owner,
            data['owner']
        )
        


class CategoryDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.category= Category(owner='owner', name='cajone', description='description')
        self.category.save()
        self.url = reverse('api-category-details', kwargs={'version': 'v1', 'pk': self.category.id})

    def test_get_category_details(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        self.assertEquals(
            data['id'],
            str(self.category.id)
        )
        self.assertEquals(
            self.category.name,
            data['name']
        )
        self.assertEquals(
            self.category.owner,
            data['owner']
        )

    def test_update_category(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        data['owner'] = 'the owner'
        data['name'] = 'name'
        data['description'] = 'description'
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.category.refresh_from_db()
        self.assertEquals(
            self.category.name,
            data['name']
        )
        self.assertEquals(
            self.category.owner,
            data['owner']
        )

    def test_delete_post(self):
        self.assertEquals(
            Category.objects.count(),
            1
        )
        response = self.client.delete(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEquals(
            Category.objects.count(),
            0
        )


#ORGANISATION TEST
class OrganisationListCreateAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('api-organisation-list', kwargs={'version': 'v1'})

    def test_create_organisation(self):
        self.assertEquals(
            Organisation.objects.count(),
            0
        )
        Category.objects.create(
            owner='owner', name='catone', description='description',  
        )
        oneCat=Category.objects.get(name='catone')
        id=oneCat.id
        print(id)
        
        data = {
            'owner':'owner', 
            'name':'catone',
            'description':'description',  
            'category':id
        }
        
        response = self.client.post(self.url, data=data,)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Organisation.objects.count(),
            1
        )
        organisation=Organisation.objects.first()
        self.assertEquals(
            organisation.name,
            data['name']
        )
        self.assertEquals(
            organisation.owner,
            data['owner']
        )

    def test_get_category_list(self):
        #tag = Tag(name='tag_name')
        #tag.save()
        Category.objects.create(
            owner='owner', name='cone', description='description',  
        )
        oneCat=Category.objects.get(name='cone')
        organisation=Organisation(owner='proprio', name='cat', description='descript', category=oneCat)
        organisation.save()
        #post.tags.add(tag)

        response = self.client.get(self.url, format='json')
        response_json = response.json()

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        

        self.assertEquals(
            len(response_json),
            4
        )
        data = response_json['results'][0]
        
        #print(data)
        self.assertEquals(
            organisation.name,
            data['name']
        )
        self.assertEquals(
            organisation.owner,
            data['owner']
        )
        


class OrganisationDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        Category.objects.create(
            owner='prop', name='catoe', description='descripton',  
        )
        oneCat=Category.objects.get(name='catoe')
        self.organisation= Organisation(owner='owner', name='cajone', description='description', category=oneCat)
        self.organisation.save()
        self.url = reverse('api-organisation-details', kwargs={'version': 'v1', 'pk': self.organisation.id})

    def test_get_organisation_details(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        self.assertEquals(
            data['id'],
            str(self.organisation.id)
        )
        self.assertEquals(
            self.organisation.name,
            data['name']
        )
        self.assertEquals(
            self.organisation.owner,
            data['owner']
        )

    def test_update_organisation(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        data['owner'] = 'the owner'
        data['name'] = 'name'
        data['description'] = 'description'
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.organisation.refresh_from_db()
        self.assertEquals(
            self.organisation.name,
            data['name']
        )
        self.assertEquals(
            self.organisation.owner,
            data['owner']
        )

    def test_delete_post(self):
        self.assertEquals(
            Organisation.objects.count(),
            1
        )
        response = self.client.delete(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEquals(
            Organisation.objects.count(),
            0
        )        