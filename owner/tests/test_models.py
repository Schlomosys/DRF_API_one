from django.test import TestCase

from owner.models import Category, Organisation


class CategoryTestCase(TestCase):
    def test_post(self):
        self.assertEquals(
            Category.objects.count(),
            0
        )
        Category.objects.create(
            owner='owner', name='name', description='description',  
        )
        Category.objects.create(
            owner='owner', name='name', description='description', 
        )
        self.assertEquals(
            Category.objects.count(),
            2
        )
        #active_category = Category.objects.
        #self.assertEquals(
           # active_category.count(),
            #1
        #)
        #inactive_category  = Category.objects.inactive()
        #self.assertEquals(
          #  inactive_category.count(),
          #  1
        #)


class OrganisationTestCase(TestCase):
    def test_post(self):
        self.assertEquals(
            Organisation.objects.count(),
            0
        )
        Category.objects.create(
            owner='owner', name='catone', description='description',  
        )
        oneCat=Category.objects.get(name='catone')
        Organisation.objects.create(
            owner='owner', name='name', description='description', category=oneCat
        )
        Organisation.objects.create(
            owner='owner', name='name', description='description', category=oneCat
        )
        self.assertEquals(
            Organisation.objects.count(),
            2
        )
        