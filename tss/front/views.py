from django.shortcuts import render
from django.http import JsonResponse


from django.core.paginator import Paginator
from country_info_tree.models import province, division, district, tehsil
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.



















# def mvalidation(request): 
#     email = request.POST.get("email", None)   
#     if email:
#         try:
#             validate_email(email)
#         except ValidationError as e:
#             res = JsonResponse({'msg': 'Invalid Email' })
#         else:
#             if queries.objects.filter(email = email).count() == 1:
#                 res = JsonResponse({'msg': 'Email Address already exists'})
#             else:
#                 res = JsonResponse({'msg': 'Email is available'})
#     else:
#         res = JsonResponse({'msg': 'Email is required.'})
#     return res

# def download_file(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/pdf")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404


# division view api start
class DivisionList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        province=request.data['province']
        print('province')
        division={}
        if province:
            divisions=province.objects.get(id=province).divisions.all()
            division={p.name:p.id for p in divisions}
        return JsonResponse(data=division, safe=False)
# division view api end

# district view api start
class DistrictList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        division=request.data['division']
        district={}
        if division:
            districts=division.objects.get(id=division).districts.all()
            district={p.name:p.id for p in districts}
        return JsonResponse(data=district, safe=False)
# district view api end

# tehsil view api start
class TehsilList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        district=request.data['district']
        tehsil={}
        if district:
            tehsils=district.objects.get(id=district).tehsils.all()
            tehsil={p.name:p.id for p in tehsils}
        return JsonResponse(data=tehsil, safe=False)
# tehsil view api end

# city view api start
class CityList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        tehsil=request.data['tehsil']
        city={}
        if tehsil:
            citys=tehsil.objects.get(id=tehsil).citys.all()
            city={p.name:p.id for p in citys}
        return JsonResponse(data=city, safe=False)
# city view api end