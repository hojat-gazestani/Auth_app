from django.shortcuts import render
from django.http import HttpResponse
import socket

hostname = socket.gethostname()

def auth_root(request):
    return HttpResponse(f"auth on {hostname}")
    
def auth1(request):
    return HttpResponse(f"auth1 on {hostname}")
    
def auth2(request):
    return HttpResponse(f"auth2 on {hostname}")
