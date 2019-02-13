"""APIView_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^publisher/$', views.PublisherView.as_view()),
    # url(r'^publisher/(\d+)/$', views.PublisherDetailView.as_view()), #不加超链接
    url(r'^publisher/(?P<pk>\d+)/', views.PublisherDetailView.as_view(), name="publisher_detail"), #加超链接
    #执行流程PublisherDetailView是一个类，调用as_view()方法返回值view，实际上是执行APIView的父类(View)中as_view()中的view，
    #view的执行实际上是dispatch方法的执行，dispatch返回什么view就返回什么，APIView中有dispatch方法，执行APIView中的dispatch
    #dispatch中的handle通过getattr找到对应PublisherDetailView中的get.post,put,delete方法


    url(r'^books/$', views.BookView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
]
