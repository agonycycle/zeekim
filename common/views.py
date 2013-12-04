# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
import datetime

def test(request):
	return render(request, 'readme.html',{})

def main(request):
    return render(request, 'main.html', {})
