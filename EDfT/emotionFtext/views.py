from django.shortcuts import render
from django.http import HttpResponse
from numpy import array

# Create your views here.

def index(request):
    return render(request,"home.html")

# def train(request):

def predict(request):
    # if 'textfile' in request.POST and 'textfile' not in request.FILES and len(request.POST['sentences']) == 0:
    #     return HttpResponse("DATA NOT FOUND!")
    # sentences = request.POST['sentences']
    # if 'textfile' not in request.POST:
    #     textfile = request.FILES['textfile'].read().decode('utf-8')
    # else:
    #     textfile = []
    # all_sentences = []

    # return render(request, 'predict.html',{'result': result,
    #                                         'emo0': result['counters'][0],
    #                                         'emo1': result['counters'][1],
    #                                         'emo2': result['counters'][2],
    #                                         'emo3': result['counters'][3],
    #                                         'emo4': result['counters'][4],
    #                                         'emo5': result['counters'][5]})
    return render(request, 'predict.html',{ 'emo0': 50,
                                            'emo1': 20,
                                            'emo2': 15,
                                            'emo3': 10,
                                            'emo4': 3,
                                            'emo5': 2})
