from django.shortcuts import render

# Create your views here.
# Services view start
def services(request):
    return render(request, 'services/service.html', {'title': 'Our Services'})
# Services view end