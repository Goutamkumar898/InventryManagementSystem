from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Supplier, SaleOrder
from .serializers import ProductSerializer, SupplierSerializer, SaleOrderSerializer

@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Product added successfully!"})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_supplier(request):
    serializer = SupplierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Supplier added successfully!"})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def list_suppliers(request):
    suppliers = Supplier.objects.all()
    serializer = SupplierSerializer(suppliers, many=True)
    return Response(serializer.data)

