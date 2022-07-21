from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import blogs,users

#url: localhost:8000/posts/{post_id}
#method: post
#data: (postId:7, userId:5, "title":"Good Morning", "content":"Hello")
class PostView(APIView):

    def get(self,request,*args,**kwargs):
        if "limit" in request.query_params:
            limit=int(request.query_params.get("limit"))
            data=blogs[0:limit]
            return Response(data=data)

        if "liked_by" in request.query_params:
            id=int(request.query_params.get("liked_by"))
            liked_post=[blog for blog in blogs if id in blog["liked_by"]]
            return Response(data=liked_post)

        return Response({"data":blogs})

    def post(self,request,*args,**kwargs):
        blog=request.data
        blogs.append(blog)
        return Response(data=blog)

#url : social/posts/{pid}
class PostDetailView(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        blog=[b for b in blogs if b["postId"]==pid].pop()
        return Response(data=blog)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        blog=[b for b in blogs if b["postId"]==id].pop()
        blogs.remove(blog)
        return Response(data=blog)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        blog=[b for b in blogs if b["postId"]==id].pop()
        blog.update(request.data)
        return Response(data=blog)

# url: social/posts/likes/<int:pid>
# method: post
# data: {"userid":1}
class AddLikeView(APIView):
    def post(self,request,*args,**kwargs):
        post_id=kwargs.get("pid")
        blog=[b for b in blogs if b["postId"]==post_id].pop()
        user=request.data.get("userid")
        blog["liked_by"].append(user)
        return Response(data=blog)

#url:localhost:8000/posts?liked_by=2
#method:get

#request.query_params

# Query_Parameter ==>