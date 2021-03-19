from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from .models import wordembedded
from flask import Flask, render_template, request, redirect

#Import Module 
import os 
from nltk.tokenize import sent_tokenize, word_tokenize 
import gensim 
from gensim.models import Word2Vec
from gensim.models import FastText
from bpemb import BPEmb
#SENTENCE EMBEDDING
#Creating Doc2Vec Model
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
# Folder Path 
global keepScore2
keepScore2 =""
class Test:
    def __init__(self):
        path = r"C:\Users\ihasa\OneDrive\Desktop\dataset" 
        file = os.listdir(path) 
        data = [] 
        for i in file:
            if i.endswith(".txt"):
                opening = open(path+"\\"+ i, "r", encoding = "utf-8")
                reading = opening.read()
                f = reading.replace("\n", " ")
                #Tokenization 
                #Iterating through each sentence in the file 
                for i in sent_tokenize(f): 
                    temp = []
                    #Tokenizing the sentence into words 
                    for j in word_tokenize(i): 
                        temp.append(j.lower())
                    data.append(temp)
        model1 = gensim.models.Word2Vec(data, min_count = 1, size = 100, window = 5) 
        #Creating Skip Gram model 
        model2 = gensim.models.Word2Vec(data, min_count = 1, size = 100, window = 5, sg = 1) 
        #Creating FastText Model
        model3 = FastText(size = 4, window = 3, min_count = 1)  # instantiate
        model3.build_vocab(sentences = data)
        model3.train(sentences=data, total_examples = len(data), epochs = 10)
        tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(data)]
        modelDoc2vec = Doc2Vec(tagged_data, vector_size = 20, window = 2, min_count = 1, epochs = 100)
        # type(bpemb_az.emb)
        self.bpemb_az = BPEmb(lang="az")
        self.bpemb_az1 = BPEmb(lang="az", vs=100000)
        # self.bpemb_az.vectors.shape
        self.model = model1
        self.model2 = model2 
        self.model3 = model3
        self.modelDoc2vecc = modelDoc2vec
        self.file = file
        self.keepEncode=0 
 
    def modelDoc2vec(self):
        vocabs = self.modelDoc2vecc.wv.vocab
        return vocabs

    def modelSenEmSim(self):
        for i in self.file: 
            if i.endswith(".txt"):
                test_doc = word_tokenize(i.lower())
                test_doc_vector = self.modelDoc2vecc.infer_vector(test_doc)
        similarity = self.modelDoc2vecc.docvecs.most_similar(positive = [test_doc_vector])
        return similarity
   
    def getModelSimilarity(self,wordOne,wordTwo,modelType):
        if wordOne == '' or wordTwo=='' or modelType=='':
            return None
        elif modelType == "cbowm":
            similarity = self.model.similarity(wordOne,wordTwo)
            return similarity
        elif modelType == "sgm":
            similarity = self.model2.similarity(wordOne,wordTwo)
            return similarity
        elif modelType == "ftm":
            similarity = self.model3.similarity(wordOne,wordTwo)
            return similarity

    def getModelMostSimilarity(self,Word,modelType,encodeornot):
        if Word=='' or modelType=='':
            return None
        elif modelType == "cbowm":
            mostSimilarity = self.model.wv.most_similar(Word)
            self.keepEncode = 0
            return mostSimilarity
        elif modelType == "sgm":
            mostSimilarity = self.model2.wv.most_similar(Word)
            self.keepEncode = 0
            return mostSimilarity
        elif modelType == "ftm":
            mostSimilarity = self.model3.wv.most_similar(Word)
            self.keepEncode = 0
            return mostSimilarity
        elif modelType == "scrum" and encodeornot != "Encode":
            mostSimilarity = self.bpemb_az.most_similar(Word, topn=10)
            self.keepEncode = 0
            return mostSimilarity
        elif modelType == "scrum" and encodeornot == "Encode":
            mostSimilarity = self.bpemb_az1.encode(Word) 
            self.keepEncode = 1
            return mostSimilarity

global newtest
newtest = Test() 
def home(request):
    return render(request,"index.html",{"resultSim":"empty","result":"empty","resultEncode":"empty","resultDoc2Vector":"empty","resultSenEmSim":"empty"})

     
def findSim(request):
    getWord1=request.GET["word1"]
    getWord2=request.GET["word2"]
    modelType=request.GET["modelTypeHidden"]
    score =  newtest.getModelSimilarity(getWord1,getWord2,modelType)
    if score is None:
        return render(request,"index.html",{"emptyInputs":"Please select model or fill all inputs","resultDoc2Vector":"empty","resultSenEmSim":"empty","resultSim":"empty","result":"empty","resultEncode":"empty"}) 
    else:
        return render(request,"index.html",{"resultSim":score,"result":"empty","resultEncode":"empty","resultDoc2Vector":"empty","resultSenEmSim":"empty","modelType":modelType}) 
  
def getVocabSenEmbe(request):
    score =  newtest.modelDoc2vec()
    modelType=request.GET["modelTypeHidden"]
    if score is None:
        return render(request,"index.html",{"emptyInputs":"Please select model or fill all inputs","resultDoc2Vector":"empty","resultSenEmSim":"empty","resultSim":"empty","result":"empty","resultEncode":"empty"}) 
    else:
        return render(request,"index.html",{"resultDoc2Vector":score,"resultSim":"empty","result":"empty","resultDoc2Vec":"empty","resultSenEmSim":"empty","resultEncode":"empty","modelType":modelType}) 

def getSimiSenEmbe(request):
    modelType=request.GET["modelTypeHidden"]
    score =  newtest.modelSenEmSim()
    if score is None:
        return render(request,"index.html",{"emptyInputs":"Please select model or fill all inputs","resultDoc2Vector":"empty","resultSenEmSim":"empty","resultSim":"empty","result":"empty","resultEncode":"empty"}) 
    else:
        return render(request,"index.html",{"resultSenEmSim":score,"resultSim":"empty","result":"empty","resultDoc2Vector":"empty","resultEncode":"empty","modelType":modelType}) 
 
def findMostSim(request):
    singleWord=request.GET["wordsingle"]
    modelType=request.GET["modelTypeHidden"] 
    endodeornot = request.GET["endodeornot"]
    listOfResult =  newtest.getModelMostSimilarity(singleWord,modelType,endodeornot)
    if listOfResult is None:
        return render(request,"index.html",{"emptyInputs":"Please select model or fill all inputs","resultDoc2Vec":"empty","resultSenEmSim":"empty","resultSim":"empty","result":"empty","resultEncode":"empty"}) 
    else:
        if newtest.keepEncode == 1:
            return render(request,"index.html",{"resultEncode":listOfResult,"result":"empty","resultSim":"empty","modelType":modelType}) 
        else:
            return render(request,"index.html",{"result":listOfResult,"resultSim":"empty","resultDoc2Vec":"empty","resultSenEmSim":"empty","resultEncode":"empty","modelType":modelType}) 
 