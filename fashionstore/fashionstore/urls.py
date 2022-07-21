"""fashionstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fashionAPI import views
from posts import views as pview
from products import views as prview

urlpatterns = [
    path('admin/', admin.site.urls),
    path("helloworld/",views.HelloWorldView.as_view()),
    path("goodmorning/", views.GoodMorningView.as_view()),
    path("welcome/", views.WelcomeView.as_view()),
    path("hi/", views.HiView.as_view()),
    path("greetings/",views.GreetingsView.as_view()),
    path("operations/add/",views.AddNumbersView.as_view()),
    path("operations/cube/",views.CubeView.as_view()),
    path("operations/factorial/",views.FactorialView.as_view()),
    path("operations/wc/",views.WordCountView.as_view()),
    path("social/posts/",pview.PostView.as_view()),
    path("social/posts/<int:pid>/",pview.PostDetailView.as_view()),
    path("store/products/",prview.ProductView.as_view()),
    path("store/products/<int:prid>/",prview.ProductDetailsView.as_view()),
    path("social/posts/likes/<int:pid>/",pview.AddLikeView.as_view()),
]
