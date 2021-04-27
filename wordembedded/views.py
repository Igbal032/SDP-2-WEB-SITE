from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from .models import wordembedded
from flask import Flask, render_template, request, redirect
from gensim.models import KeyedVectors
class Models: 
    def __init__(self):
        #Creating CBOW WORD2VEC model 
        modelW2VCbow = KeyedVectors.load_word2vec_format("CBOWw2v.txt")
        #Creating Skip Gram WORD2VEC model 
        modelW2VSG = KeyedVectors.load_word2vec_format("SGw2v.txt")
        #Creating CBOW FastText Model
        modelFTCBOW = KeyedVectors.load_word2vec_format("CBOWFT.txt")
        #Creating Skip Gram FastText Model
        modelFTSG = KeyedVectors.load_word2vec_format("SGFT.txt")
        self.modelW2VCbow = modelW2VCbow 
        self.modelW2VSG = modelW2VSG 
        self.modelFTCBOW = modelFTCBOW
        self.modelFTSG = modelFTSG
    
    def getAnalogy(self,positive1,positive2,negative,modelType):
        if positive1 == '' or positive2=='' or modelType=='' or negative=='': 
            return None 
        elif modelType == "cbown":
            try:
                analogy = self.modelW2VCbow.most_similar(positive = [positive1.lower(),positive2.lower()], negative = [negative.lower()],topn=1)
                return analogy
            except:
                analogy = "error"
                return analogy
        elif modelType == "sgm":
            try:
                analogy = self.modelW2VSG.most_similar(positive = [positive1.lower(),positive2.lower()], negative = [negative.lower()],topn=1)
                return analogy
            except:
                analogy = "error"
                return analogy
        elif modelType == "ftm": 
            try:
                analogy = self.modelFTCBOW.most_similar(positive = [positive1.lower(),positive2.lower()], negative = [negative.lower()],topn=1)
                return analogy
            except:
                analogy = "error"
                return analogy
        elif modelType == "sgftm": 
            try:
                analogy = self.modelFTSG.most_similar(positive = [positive1.lower(),positive2.lower()], negative = [negative.lower()],topn=1)
                return analogy
            except:
                analogy = "error"
                return analogy

    def getModelSimilarity(self,wordOne,wordTwo,modelType):
        if wordOne == '' or wordTwo=='' or modelType=='': 
            return None 
        elif modelType == "cbown":
            try:
                similarity = self.modelW2VCbow.similarity(wordOne.lower(),wordTwo.lower())
                return similarity
            except:
               similarity = "error"
               return similarity
        elif modelType == "sgm":
            try:
                similarity = self.modelW2VSG.similarity(wordOne.lower(),wordTwo.lower())
                return similarity
            except:
                similarity = "error"
                return similarity
        elif modelType == "ftm": 
            try:
                similarity = self.modelFTCBOW.similarity(wordOne.lower(),wordTwo.lower())
                return similarity
            except:
                similarity = "error"
                return similarity
        elif modelType == "sgftm": 
            try:
                print("sgft try  in icindeyem")
                similarity = self.modelFTSG.similarity(wordOne.lower(),wordTwo.lower())
                return similarity
            except:
                print("sgft exception  in icindeyem")
                similarity = "error"
                return similarity

    def getModelMostSimilarity(self,Word,modelType):
        if Word=='' or modelType=='':
            return None
        elif modelType == "cbown":
            try:
                mostSimilarity = self.modelW2VCbow.wv.most_similar(Word.lower(), topn=5)
                return mostSimilarity
            except:
                mostSimilarity = "error"
                return mostSimilarity
        elif modelType == "sgm":
            try:
                mostSimilarity = self.modelW2VSG.wv.most_similar(Word.lower(), topn=5)
                return mostSimilarity
            except:
                mostSimilarity = "error"
                return mostSimilarity
        elif modelType == "ftm":
            try:
                mostSimilarity = self.modelFTCBOW.wv.most_similar(Word.lower(), topn=5)
                return mostSimilarity
            except:
                mostSimilarity = "error"
                return mostSimilarity
        elif modelType == "sgftm":
            try:
                mostSimilarity = self.modelFTSG.wv.most_similar(Word.lower(), topn=5)
                return mostSimilarity
            except:
                mostSimilarity = "error"
                return mostSimilarity

global newModels
newModels = Models() 
def home(request): 
    return render(request,"index.html",{"resultSim":"empty","result":"empty"})

def sdpPage(request):
    return render(request,"SDP.html")

def CBOWW2VPage(request):
    return render(request,"CBOWW2V.html",{"resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"})

def SGW2VPage(request):
    return render(request,"SGW2V.html",{"resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"})

def CBOWFTPage(request):
    return render(request,"CBOWFT.html",{"resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"})
 
def AuthorsPage(request):
    return render(request,"authors.html")
  
def SGFTPage(request):
    return render(request,"SGFT.html",{"resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"})
 
     
def findSim(request):
    getWord1=request.GET["word1"]
    getWord2=request.GET["word2"]
    modelType=request.GET["modelTypeHidden"]
    score =  newModels.getModelSimilarity(getWord1,getWord2,modelType)
    if score is None:
        if modelType == 'cbown':
            return render(request,"CBOWW2V.html",{"emptyInputs1":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == "sgm":
            return render(request,"SGW2V.html",{"emptyInputs1":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == "ftm":
            return render(request,"CBOWFT.html",{"emptyInputs1":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == "sgftm":
            return render(request,"SGFT.html",{"emptyInputs1":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
    elif score == "error":
        if modelType == 'cbown':
            return render(request,"CBOWW2V.html",{"wrongWord1":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == 'sgm':
            return render(request,"SGW2V.html",{"wrongWord1":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == "ftm":
            return render(request,"CBOWFT.html",{"wrongWord1":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == "sgftm":
            return render(request,"SGFT.html",{"emptyInputs1":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
    else:
        if modelType == 'cbown':
            return render(request,"CBOWW2V.html",{"resultSim":score,"word1":getWord1,"word2":getWord2, "resultMostSim":"empty","modelType":modelType,"resultForAnalogy":"empty"}) 
        elif modelType == 'sgm':
            return render(request,"SGW2V.html",{"resultSim":score,"word1":getWord1,"word2":getWord2, "resultMostSim":"empty","modelType":modelType,"resultForAnalogy":"empty"}) 
        elif modelType == "ftm":
            return render(request,"CBOWFT.html",{"resultSim":score,"word1":getWord1,"word2":getWord2, "resultMostSim":"empty","modelType":modelType,"resultForAnalogy":"empty"}) 
        elif modelType == "sgftm":
            return render(request,"SGFT.html",{"resultSim":score,"word1":getWord1,"word2":getWord2, "resultMostSim":"empty","modelType":modelType,"resultForAnalogy":"empty"}) 

def findMostSim(request):  
    singleWord=request.GET["wordsingle"] 
    modelType=request.GET["modelTypeHidden"] 
    listOfResult =  newModels.getModelMostSimilarity(singleWord,modelType)
    if listOfResult is None:
        if modelType == 'cbown':
            return render(request,"CBOWW2V.html",{"emptyInputs2":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == 'sgm':
            return render(request,"SGW2V.html",{"emptyInputs2":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == 'ftm':
            return render(request,"CBOWFT.html",{"emptyInputs2":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == 'sgftm':
            return render(request,"SGFT.html",{"emptyInputs2":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        else:
            return render(request,"index.html",{"emptyInputs":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"})
    elif listOfResult == "error":
        if modelType == 'cbown':
            return render(request,"CBOWW2V.html",{"wrongWord2":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == 'sgm':
            return render(request,"SGW2V.html",{"wrongWord2":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == 'ftm':
            return render(request,"CBOWFT.html",{"wrongWord2":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == "sgftm":
            return render(request,"SGFT.html",{"wrongWord2":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
    else:
        if modelType == 'cbown':
            return render(request,"CBOWW2V.html",{"resultMostSim":listOfResult,"singleWord":singleWord,"resultSim":"empty","modelType":modelType,"resultForAnalogy":"empty"}) 
        elif modelType == 'sgm':
            return render(request,"SGW2V.html",{"resultMostSim":listOfResult,"singleWord":singleWord,"resultSim":"empty","modelType":modelType,"resultForAnalogy":"empty"}) 
        elif modelType == 'ftm':
            return render(request,"CBOWFT.html",{"resultMostSim":listOfResult,"singleWord":singleWord,"resultSim":"empty","modelType":modelType,"resultForAnalogy":"empty"}) 
        elif modelType == 'sgftm':
            return render(request,"SGFT.html",{"resultMostSim":listOfResult,"singleWord":singleWord,"resultSim":"empty","modelType":modelType,"resultForAnalogy":"empty"}) 
        else: 
            return render(request,"index.html",{"emptyInputs":"Error Occured","resultSim":"empty","resultMostSim":"empty","modelType":modelType,"resultForAnalogy":"empty"}) 
  
def findAnalogy(request):
    modelType=request.GET["modelTypeHidden"]  
    positive1=request.GET["positive1"]  
    positive2=request.GET["positive2"]  
    negative=request.GET["negative"] 
    analogyRes = newModels.getAnalogy(positive1,positive2,negative,modelType)
    print(analogyRes)
    if analogyRes is None:
        if modelType == 'cbown': 
            return render(request,"CBOWW2V.html",{"emptyInputs3":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == 'sgm':
            return render(request,"SGW2V.html",{"emptyInputs3":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == 'sgm':
            return render(request,"SGW2V.html",{"emptyInputs3":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == 'ftm':
            return render(request,"CBOWFT.html",{"emptyInputs3":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == 'sgftm':
            return render(request,"SGFT.html",{"emptyInputs3":"Please, fill the inputs","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
    elif analogyRes == "error":
        if modelType == 'cbown':
            return render(request,"CBOWW2V.html",{"wrongWord3":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == 'sgm':
            return render(request,"SGW2V.html",{"wrongWord3":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == "ftm":
            return render(request,"CBOWFT.html",{"wrongWord3":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
        elif modelType == "sgftm":
            return render(request,"SGFT.html",{"wrongWord3":"Entered word(s) is/are not in data","resultSim":"empty","resultMostSim":"empty","resultForAnalogy":"empty"}) 
    else:
        if modelType == 'cbown':
            return render(request,"CBOWW2V.html",{"resultForAnalogy":analogyRes,"positive1":positive1,"positive2":positive2,"negative":negative,"resultSim":"empty","resultMostSim":"empty","modelType":modelType}) 
        elif modelType == 'sgm':
            return render(request,"SGW2V.html",{"resultForAnalogy":analogyRes,"positive1":positive1,"positive2":positive2,"negative":negative,"resultSim":"empty","resultMostSim":"empty","modelType":modelType}) 
        elif modelType == 'ftm':
            return render(request,"CBOWFT.html",{"resultForAnalogy":analogyRes,"positive1":positive1,"positive2":positive2,"negative":negative,"resultSim":"empty","resultMostSim":"empty","modelType":modelType}) 
        elif modelType == 'sgftm':
            return render(request,"SGFT.html",{"resultForAnalogy":analogyRes,"positive1":positive1,"positive2":positive2,"negative":negative,"resultSim":"empty","resultMostSim":"empty","modelType":modelType})  