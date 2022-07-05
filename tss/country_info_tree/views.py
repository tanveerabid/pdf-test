from django.shortcuts import render

from .models import *
import json
# Create your views here.
def indexview(request):
    province=province.objects.all().order_by('name')
    province_list=list(province.values('name','id'))
    province_list=json.dumps(province_list)

    division=division.objects.all().order_by('name')
    division_list=list(division.values('name','country__name','id'))
    division_list=json.dumps(division_list)

    district=district.objects.all().order_by('name')
    district_list=list(district.values('name','division__name','id'))
    district_list=json.dumps(district_list)

    tehsil=tehsil.objects.all().order_by('name')
    tehsil_list=list(tehsil.values('name','district__name','id'))
    tehsil_list=json.dumps(tehsil_list)

    city=city.objects.all().order_by('name')
    city_list=list(city.values('name','district__name','id'))
    city_list=json.dumps(city_list)

    context={
        "province_list":province_list,
        "division_list":division_list,
        "district_list":district_list,
        "tehsil_list":tehsil_list,
        "city_list":city_list,
    }
    return render(request, 'index.html',context)



# from .models import Contact
# from .serializers import ContactSerializer
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# class ContactListCreateAPIView(ListCreateAPIView):
#     serializer_class=ContactSerializer
#     queryset=Contact.objects.all()
# class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class=ContactSerializer
#     queryset=Contact.objects.all()
#     lookup_field='id'