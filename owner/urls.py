from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('categorypost/',views.CategoryListCreateAPIView.as_view(), name='api-category-list'),
    path('categorypost/',views.CategoryCreateAPIView.as_view(), name='api-category-creater'),
    path('categoryget/',views.CategoryListAPIView.as_view(), name='api-category-lister'),
    path('categories/<uuid:pk>/', views.CategoryDetailsAPIView.as_view(), name='api-category-details'),
    path('organisation/',views.OrganisationListCreateAPIView.as_view(), name='api-organisation-list'),
    path('organisations/<uuid:pk>/', views.OrganisationDetailsAPIView.as_view(), name='api-organisation-details'),
    path('qrgen/',views.CreateQRView.as_view(), name='api-qr-create'),
]