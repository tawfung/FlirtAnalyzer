from numpy import array
from django.shortcuts import render
from django.http import HttpResponse
from detector.deep_learn.learn import *
from detector.deep_learn.predict import *
from detector.deep_learn.vectorization import *

# Create your views here.
def index(request):
    return render(request,"home.html")

def train(request):
    vectorizer = Vectorizer()
    vectorizer.start(mode = 'train', text=None)
    trainer = Trainer()
    acc = trainer.start()

    return HttpResponse(acc)

def predict(request):
    if 'textfile' in request.POST and 'textfile' not in request.FILES and len(request.POST['sentences']) == 0:
        return HttpResponse("DATA NOT FOUND!")
    sentences = request.POST['sentences']
    if 'textfile' not in request.POST:
        textfile = request.FILES['textfile'].read().decode('utf-8')
    else:
        textfile = []

    all_sentences = []
    vectorizer = Vectorizer()

    if len(sentences) != 0:
        for vector in vectorizer.start(mode='vectorize', text=sentences):
            all_sentences.append(vector)
    if len(textfile) != 0:
        for vector in vectorizer.start(mode='vectorize', text=textfile):
            all_sentences.append(vector)
    if len(all_sentences) == 0:
        return HttpResponse("DATA NOT FOUND!!!")

    print ('seee', all_sentences)
    classifier = Classifier()
    result = classifier.start(all_sentences)
    # print(result)

    return render(request, 'predict.html',{
    # 'result': result,
    #                                         'angr': result['counters'][0],
    #                                         'disg': result['counters'][1],
    #                                         'joy': result['counters'][2]})
                                            # 'emo3': result['counters'][3],
                                            # 'emo4': result['counters'][4],
                                            # 'emo5': result['counters'][5]})
    # return render(request, 'predict.html',{ 'emo0': 50,
    #                                         'emo1': 20,
    #                                         'emo2': 15,
    #                                         'emo3': 10,
    #                                         'emo4': 3,
    #                                         'emo5': 2
    })
