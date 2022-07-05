from django.shortcuts import render
from .models import *
# Create your views here.

# Verify view start
def verify(request):
    return render(request, 'verification/verify.html', {'title': 'Verfication'})
# Verify view end