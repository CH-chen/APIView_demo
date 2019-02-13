from django.shortcuts import render

from app01 import models
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

class PublisherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = "__all__"

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"

        # 以上是默认的
        # 显示超链接
    publisher = serializers.HyperlinkedIdentityField(
        view_name="publisher_detail",  # url中的别名
        lookup_field="publisher_id", #关联字段的字段名
        lookup_url_kwarg="pk",
    )
    # 默认一对多，多对多显示主键，可以自定义显示字段为name和其他字段， 可以不加就显示全部  publisher用自定义的话post请求要重写create方法
    # publisher = serializers.CharField(source="publisher.name")#一对多可以用 自定义字段
    # authors = serializers.CharField(source="authors.all") #多对多不好用
    # 多对多自定义显示字段用下面这个，默认显示主键
    # authors =serializers.SerializerMethodField() ##自定义字段
    # def get_authors(self,obj):
    #     temp = []
    #     for obj in obj.authors.all():
    #         temp.append(obj.name)
    #         print(temp)
    #     return temp
    ##自定义显示字段 用自定义的话post请求要重写create方法,不自定义用默认的就不需要create方法
    def create(self,validated_data):
        print("validated_data",validated_data)
        book = models.Book.objects.create(title=validated_data["title"],price=validated_data["price"],pub_date=validated_data["pub_date"],publisher_id=validated_data["publisher"]["pk"])
        book.authors.add(*validated_data["authors"])
        return book

class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"


class PublisherView(APIView):

    #获取所有出版社
    def get(self,request):

        pub_list = models.Publisher.objects.all()
        pub_ser = PublisherModelSerializer(pub_list,many=True)
        return Response(pub_ser.data)
    #提交出版社
    def post(self,request):
        print(request._request.body)
        print(request._request.POST)
        print("==========")
        print(request.data)


        pub_ser = PublisherModelSerializer(data=request.data)
        if pub_ser.is_valid():
            print(pub_ser.validated_data)
            pub_ser.save()
            return Response(pub_ser.data)
        else:
            return Response(pub_ser.errors)

class PublisherDetailView(APIView):
    #查看某个出版社
    def get(self,request,pk):
        pub_obj = models.Publisher.objects.filter(pk=pk).first()
        pub_ser = PublisherModelSerializer(pub_obj)
        return Response(pub_ser.data)
    #更新某个出版社 提交的时候id可以不写，其他字段都不能少，否则报错
    def put(self,request,pk):
        pub_obj = models.Publisher.objects.filter(pk=pk).first()
        pub_ser = PublisherModelSerializer(pub_obj,data=request.data)
        if pub_ser.is_valid():
            pub_ser.save()
            return Response(pub_ser.data)
        else:
            return Response(pub_ser.errors)
    #删除某个出版社
    def delete(self,request,pk):
        models.Publisher.objects.filter(pk=pk).delete()
        return Response()

class BookView(APIView):

    def get(self,request):
        #http://127.0.0.1:8000/books/?a=1&b=2
        print(request._request.body) #b''  request._request.body区的是请求体的数据，GET没有请求体为空
        print(request._request.GET)  #<QueryDict: {'a': ['1'], 'b': ['2']}>#取到的是url中的数据

        book_list = models.Book.objects.all()
        book_ser = BookModelSerializer(book_list,many=True,context={"request": request})  #如果有超链接的话要加context={"request":request}
        return Response(book_ser.data)

    def post(self,request):
        print(request.data)
        book_ser = BookModelSerializer(data=request.data)
        print(book_ser)
        print("========")
        print(book_ser.publisher)
        if book_ser.is_valid():
            print(book_ser.validated_data)
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response(book_ser.errors)

class BookDetailView(APIView):

    def get(self,request,pk):
        book_obj = models.Book.objects.filter(pk=pk).first()
        book_ser = BookModelSerializer(book_obj,context={"request":request}) #如果有超链接的话要加context={"request":request}
        return Response(book_ser.data)

    def put(self,request,pk):
        book_obj = models.Book.objects.filter(pk=pk).first()
        book_ser = BookModelSerializer(book_obj,data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response(book_ser.errors)

    def delete(self,request,pk):
        models.Book.objects.filter(pk=pk).delete()
        return Response()
