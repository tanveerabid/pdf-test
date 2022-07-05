from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from django.http import JsonResponse

class DivisionListAPIView(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        prov = request.data['province']
        div = {}
        if prov:
            divs = division.objects.all().filter(province=prov)
            div = {pp.name:pp.id for pp in divs}
        return JsonResponse(data=div, safe=False)

class DistrictListAPIView(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        div = request.data['division']
        dis = {}
        if div:
            dists = district.objects.all().filter(division=div)
            dis= {pp.name:pp.id for pp in dists}
        return JsonResponse(data=dis, safe=False)

class TehsilListAPIView(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        dist = request.data['district']
        teh = {}
        if district:
            tehsils = tehsil.objects.all().filter(district=dist)
            teh = {pp.name:pp.id for pp in tehsils}
        return JsonResponse(data=teh, safe=False)

class PhoneCodeListAPIView(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        dist = request.data['district']
        code = {}
        if district:
            phn_codes = phn_code.objects.all().filter(district=dist)
            code = {pp.code:pp.id for pp in phn_codes}
        return JsonResponse(data=code, safe=False)