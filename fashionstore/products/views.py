from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import products

class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        if "limit" in request.query_params:
            limit=int(request.query_params.get("limit"))
            data=products[0:limit]
            return Response(data=data)

        return Response({"data":products})
    def post(self,request,*args,**kwargs):
        product=request.data
        products.append(product)
        return Response(data=product)

#url: store/products/{prid}
class ProductDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        prid=kwargs.get("prid")
        product=[p for p in products if p["id"]==prid].pop()
        return Response(data=product)

    def delete(self,request,*args,**kwargs):
        prid=kwargs.get("prid")
        product=[b for b in products if b["id"]==prid].pop()
        products.remove(product)
        return Response(data=product)

    def put(self,request,*args,**kwargs):
        prid=kwargs.get("prid")
        product=[b for b in products if b["id"]==prid].pop()
        product.update(request.data)
        return Response(data=product)

