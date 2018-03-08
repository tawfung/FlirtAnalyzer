from django.shortcuts import render
from django.http import HttpResponse
from numpy import array

# Create your views here.

def index(request):
    return render(request,"home.html")

# def train(request):

def predict(request):
    if 'textfile' in request.POST and 'textfile' not in request.FILES and len(request.POST['sentences']) == 0:
        return HttpResponse("DATA NOT FOUND!")
    sentences = request.POST['sentences']
    if 'textfile' not in request.POST:
        textfile = request.FILES['textfile'].read().decode('utf-8')
    else:
        textfile = []
    all_sentences = []
    
    