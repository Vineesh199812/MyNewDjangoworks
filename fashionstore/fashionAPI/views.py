from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from functools import reduce
import datetime

#get,post,put,patch,delete
class HelloWorldView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"hello world"})

class GoodMorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"message":"Good Morning"})

class WelcomeView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"Msg":"Welcome"})

class HiView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"Hi":"Hi India"})


class GreetingsView(APIView):
    def get(self,request,*args,**kwargs):
        msg=""
        c_time=datetime.datetime.now()
        c_hour=c_time.hour
        if c_hour<12:
            msg="Good Morning"
        elif(c_hour<18):
            msg="Good Afternoon"
        elif(c_hour<24):
            msg="Good Night"
        return Response({"data":msg})

class AddNumbersView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2
        return Response({"msg":res})

class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n=request.data.get("num")
        res=n**3
        return Response({"msg":res})

class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        n=request.data.get("num")
        fact=reduce(lambda n1,n2:n1*n2,range(1,n+1))
        return Response({"msg":fact})

class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get("text")
        wc={}
        words=text.split(" ")
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response({"data":wc})


