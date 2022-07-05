from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages

# imports for neccessary models start
from .models import *
# imports for neccessary models end

# imports for validating email start
from django.core.validators import validate_email
# imports for validating email end

# imports for verification token generation start
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
# imports for verification token generation end

from .utils import generate_token, send_auto_email

from django.core.exceptions import ObjectDoesNotExist

# import for threading start
import threading
# import for threading end

# Create your views here.



# Contact view start
def contact(request):
    try:
        offices =  office.objects.all()
    except ObjectDoesNotExist:
        offices = None
    context = {
        'offices' : offices,
        'title': 'Contact Us'
    }
    return render(request, 'contact/contact.html', context)
# Contact view end


# query/complaint view start
def submitquery(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        name = post_data.get("name", None)
        email = post_data.get("email", None)
        phone = post_data.get("phone", None)
        subject = post_data.get("subject", None)
        message = post_data.get("message", None)
        if email:
            try:
                validate_email(email)
            except:
                res = JsonResponse({'res_code': 0,'msg': 'Invalid Email' })
            else:
                if query.objects.filter(email = email).filter(query_resolve_status = False).count() == 1:
                    res = JsonResponse({'msg': 'There is already a query pending against your email. Kindly contact at business@tss.org.pk for update.'})
                else:
                    que = query()
                    que.name = name
                    que.email = email
                    que.phone = phone
                    que.subject = subject
                    que.message = message
                    que.save()
                    subject = f'{que.subject} | Query Received'
                    mail_template = 'email-pages/query_received_mail.html'
                    receiver = [que.email, ]
                    context = {
                    'name': que.name
                    }
                    try:
                        t = threading.Thread(target=send_auto_email, args=[receiver, subject, mail_template, context, request])
                        t.start()
                        res = JsonResponse({'res_code': 1,'msg': 'Your query has been registered, we will get to you Soon!'})
                    except:
                        res = JsonResponse({'res_code': 0,'msg': 'Error, check your details or please try again later!' })
        else:
            res = JsonResponse({'res_code': 0,'msg': 'Email is required.'})
    return res
# query/complaint view end

# Subscribe view Start
def subscribe(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        if email:
            try:
                validate_email(email)
            except:
                res = JsonResponse({'res_code': 0,'msg': 'Invalid Email' })
            else:
                subject = 'Confirm Your Subscription'
                mail_template = 'email-pages/subscription_confirmation_mail.html'
                try:
                    sub = subscriber.objects.get(email = email)
                except ObjectDoesNotExist:
                    try:
                        sub1 = subscriber()
                        sub1.email = email
                        sub1.save()
                        res = JsonResponse({'res_code': 1,'msg': 'check your email to actiavte subscription!'})

                        current_site = get_current_site(request)
                        sid = urlsafe_base64_encode(force_bytes(sub1.pk))
                        token = generate_token.make_token(sub1)
                        receiver = [sub1.email, ]
                        context = {
                        'domain' : current_site,
                        'sid': sid,
                        'token': token
                        }
                        t = threading.Thread(target=send_auto_email, args=[receiver, subject, mail_template, context, request])
                        t.start()
                    except:
                        res = JsonResponse({'res_code': 0,'msg': 'Something went wrong!' })
                else:
                    if sub.is_verified == True:
                        res = JsonResponse({'res_code': 1,'msg': 'Already Subscribed!'})
                    else:
                        # send a confirmation mail
                        current_site = get_current_site(request)
                        sid = urlsafe_base64_encode(force_bytes(sub.pk))
                        token = generate_token.make_token(sub)
                        receiver = [sub.email, ]
                        context = {
                        'domain' : current_site,
                        'sid': sid,
                        'token': token
                        }
                        t = threading.Thread(target=send_auto_email, args=[receiver, subject, mail_template, context, request])
                        t.start()
                        res = JsonResponse({'res_code': 1,'msg': 'check your email to actiavte subscription!'})       
        else:
            res = JsonResponse({'res_code': 0,'msg': 'Email is required.'})
    return res


def sub_activate(request, uidb64, token):
    try:
        sid = force_str(urlsafe_base64_decode(uidb64))
        sub = subscriber.objects.get(pk=sid)

    except Exception as e:
        sub = None

    if sub and generate_token.check_token(sub, token):
        if sub.sub_status == True:
            messages.success(request, f'{sub.email} is already subscribed.', extra_tags='alert') 
            return render(request, 'email-confirmation-pages/sub-activate-complete.html')
        else:
            sub.is_verified = True
            sub.sub_status = True
            sub.save()
            current_site = get_current_site(request)
            sid = urlsafe_base64_encode(force_bytes(sub.pk))
            token = generate_token.make_token(sub)
            receiver = [sub.email, ]
            context = {
            'domain' : current_site,
            'sid': sid,
            'token': token
            }
            t = threading.Thread(target=send_auto_email, args=[receiver, subject, mail_template, context, request])
            t.start()
            messages.success(request, f'Subscription Activated Successfully for {sub.email}', extra_tags='alert') 
            return render(request, 'email-confirmation-pages/sub-activate-complete.html')
    messages.success(request, 'Sorry! your provided link is expired.', extra_tags='alert') 
    return render(request, 'email-confirmation-pages/sub-activate-fail.html')

# Subscribe view end