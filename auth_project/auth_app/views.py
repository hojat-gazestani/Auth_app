from django.shortcuts import render
from django.http import HttpResponse
import socket
from auth_project.context_processors import gunicorn_port

hostname = socket.gethostname()

def auth(request):
    return HttpResponse(f"auth on {hostname}, Gunicorn port: { gunicorn_port(request)}")
    
def auth1(request):
    return HttpResponse(f"auth1 on {hostname}, Gunicorn port: { gunicorn_port(request)}")
    
def auth2(request):
    return HttpResponse(f"auth2 on {hostname}, Gunicorn port: { gunicorn_port(request)}")
