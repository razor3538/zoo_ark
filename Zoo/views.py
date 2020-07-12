from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProductSerializer
from .models import *


class ProductView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response({"product": serializer.data})

    def post(self, request):
        product = request.data.get('product')
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            product_save = serializer.save()
        return Response({"success": "product {} added".format(product_save.name)})

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Product.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Product with id `{}` has been deleted.".format(pk)
        }, status=204)


class DetailView(APIView):
    def get(self, request):
        if request.data.get('marker_A') is None:
            product = Product.objects.filter(marker_B=request.data.get('marker_B'))
        elif request.data.get('marker_B') is None:
            product = Product.objects.filter(marker_A=request.data.get('marker_A'))
        else:
            product = Product.objects.filter(marker_A=request.data.get('marker_A'), marker_B=request.data.get('marker_B'))
        serializer = ProductSerializer(product, many=True)
        return Response({"product": serializer.data})
