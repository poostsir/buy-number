from urllib.request import urlopen
from django.http import HttpResponse
from django.shortcuts import render
from .models import IPAddress

def geting_code(request, token):
    #url_for_check = 'https://prdevs.pythonanywhere.com/blog/co/'
    url_for_check2 = 'https://prdevs.pythonanywhere.com/blog/co2/'
    #response_for_check = urlopen(url_for_check)
    response_for_check2 = urlopen(url_for_check2)
    code_for_check2 = response_for_check2.read()
    # print(code_for_check2)
    if str(code_for_check2) == "b'hello'" :
        url = f'http://canada.globalsms.io/api_gsim/v1/public/getSmsByToken?token={token}'    
        response = urlopen(url)
        code = response.read()
        context = {'code': code}
        ip_address = request.META['REMOTE_ADDR']
        if not ip_address in IPAddress.objects.all():
            IPAddress.objects.create(ip_address=ip_address)
        return render(request,"code.html",context)
    else:
        code = 'website is off'
        context = {'code': code}
        return render(request,"code.html",context)
    

def geting_code_dev(request, token):
    url_for_check2 = 'https://prdevs.pythonanywhere.com/blog/co2/'
    response_for_check2 = urlopen(url_for_check2)
    code_for_check2 = response_for_check2.read()
    if str(code_for_check2) == "b'hello'" :
        url = f'http://canada.globalsms.io/api_gsim/v1/public/getSmsByToken?token={token}'    
        response = urlopen(url)
        code = response.read()
        ip_address = request.META['REMOTE_ADDR']
        if not ip_address in IPAddress.objects.all():
            IPAddress.objects.create(ip_address=ip_address)
        return HttpResponse(code)
    else:
        code = 'website is off'
        context = {'code': code}
        return render(request,"code.html",context)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def turn_of_Or_on(request):
    return HttpResponse(True)
