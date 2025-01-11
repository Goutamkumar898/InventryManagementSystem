# inventory/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Supplier, SaleOrder, StockMovement
from .serializers import ProductSerializer, SupplierSerializer, SaleOrderSerializer, StockMovementSerializer

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailView(APIView):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

# Similarly, add views for Supplier, SaleOrder, and StockMovement
