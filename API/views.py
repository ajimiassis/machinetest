from rest_framework.decorators import APIView
from rest_framework.response import Response
from products.models import Product,Order
from API.serializers import ProductSerializer,OrderSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

class productViewSetview(APIView):
    def get(self,request,*args,**kwargs):
        qs=Product.objects.all()
        serializer = ProductSerializer(qs, many=True)
        return Response(serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        serializer=ProductSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.data)
    
    def destroy(self,requset,*args,**kwargs):
        id=kwargs.get("pk")
        Product.objects.filter(id=id).delete()
        return Response()
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        serializer=ProductSerializer(qs)
        return Response(data=serializer.data)


class OrderViewSetview(APIView):
    def get(self,request,*args,**kwargs):
        qs=Product.objects.all()
        serializer = OrderSerializer(qs, many=True)
        return Response(serializer.data)
