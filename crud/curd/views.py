# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from curd.models import Register


class Saving(APIView):
    def post(self,request):
        print(request.data,"dataaa")
        obj=Register()
        obj.eid = request.data['eid']
        obj.ename = request.data['ename']
        obj.eaddress = request.data['eaddress']
        obj.save()
        return Response("hello")

class Fetch(APIView):
    def get(self,request):
        print(request.data, "hell***************************************************888")
        details = Register.objects.all().values()
        print(request.data,"hell")
        return Response(details)

class Fetchingonedata(APIView):
    def post(self,request):
        id=request.data['eid']
        print("@@@@@2",id)
        data=Register.objects.filter(eid=id).values()
        print("##########",data)
        return Response(data)

class Editingdata(APIView):
    def post(self,request):
        id=request.data['eid']
        getdata=Register.objects.filter(eid=id)
        if getdata:
            getdata.update(ename=request.data['ename'])
            return Response(getdata)

class Removedata(APIView):
    def post(self,request):
        id=request.data['eid']
        print (id)
        data=Register.objects.filter(eid=id)
        if data:
            data.delete()
            data={"message":"delete"}
            return Response(data)
        else:
            data={"message":"not deleted"}
            return Response(data)




