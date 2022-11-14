
from itertools import product
from django.http import response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from products import serializers

from products.serializers import ProductSerializer
from .models import Product
from .serializers import ProductSerializer



@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid() ==True:
            serializer.save()
            return Response(serializer.data,status = 201)
        else:
            return Response(serializer.errors, status = 400)
         

          


    




# @api_view(['GET'])
# def product_detail(request,pk):
#     try:
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
        



     