from django.shortcuts import render
from django.http import HttpResponse
from detector.deep_learn.learn import *
from detector.deep_learn.predict import *
from detector.deep_learn.vectorization import *
from detector.deep_learn.statistical import *


# Create your views here.
def index(request):
    return render(request, "home.html")

def train(request):
    vectorizer = Vectorizer()
    vectorizer.start(mode='train', text=None)
    trainer = Trainer()
    accur = trainer.start()
    return HttpResponse(accur)

    pass

def predict(request):

    if 'textfile' in request.POST and 'textfile' not in request.FILES and len(request.POST['sentences']) == 0:
        return HttpResponse("DATA NOT FOUND!")
    # sentences = request.POST['sentences']
    sentences = request.POST.get('sentences')
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

    print('see', all_sentences)
    classifier = Classifier()
    result = classifier.start(all_sentences)
    # print(result)

    return render(request, 'predict.html', {'result': result,
                                            'ang': result['counters'][0],
                                            'sad': result['counters'][1],
                                            'joy': result['counters'][2], })

def statistical(request):
    statistics = Statistical()
    goal = statistics.stat()
    return render(request, "statistical.html",)
