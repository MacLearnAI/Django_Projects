from django.shortcuts import render
from django.http import HttpResponse
import pickle
import nltk
from nltk.tokenize import word_tokenize
import requests

with open("word_features.pickle","rb") as word_pickle:
    word_features = pickle.load(word_pickle)

with open("SGD_classifier.pickle","rb") as SGD_pickle:
    SGD_clf_pickle = pickle.load(SGD_pickle)

# Create your views here.
def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

def home(request):
   # return HttpResponse("Hello World")
   #return render(request,'home.html')
   #movie_review = request.GET['review']
   movie_review = request.GET.get('review', "None")
   print("**************",movie_review)
   if movie_review=="None":
       class_predict = ""
   else:
       class_predict = SGD_clf_pickle.classify(find_features(movie_review))
   if class_predict=="pos":
       class_predict = "Positive Review"
   else:
       class_predict="Negative Review"
   return render(request,'home.html',{'class_pred':class_predict})

