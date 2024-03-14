from django.urls import path
from API.views import productViewSetview

urlpatterns=[
    path('prod/',productViewSetview.as_view(),name="product_api")
]