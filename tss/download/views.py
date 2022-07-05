from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.

# Download document view start
def download(request):
	cat = request.GET.get('category')
	if cat:
		documents = document.objects.filter(document_category__name=cat)
		paginator = Paginator(documents, 20)
		page_obj = paginator.get_page(page_number)
		tbl_title=cat
	else:
		documents = document.objects.all()
		paginator = Paginator(documents, 20) # Show 20 contacts per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		tbl_title='all download'

	categories = document_category.objects.all()
	if categories:
		context = {
        'categories': categories,
        'page_obj': page_obj,
        'title': 'Download',
        'tbl_title':tbl_title
        }
	else:
		context = {
        'categories': categories,
        'title': 'Download',
        'tbl_title':tbl_title
        }

	return render(request, 'download/download.html', context)
# Download Document view end

def render_pdf_view(request):
    template_path = 'download/pad.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
