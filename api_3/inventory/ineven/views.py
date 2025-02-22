
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework import viewsets


# Create your views here. 
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer