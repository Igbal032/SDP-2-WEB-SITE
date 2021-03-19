# Import Module 
import os 
from nltk.tokenize import sent_tokenize, word_tokenize 
import gensim 
from gensim.models import Word2Vec
from gensim.models import FastText

#  Folder Path 
def getData():
    path = r'C:\Users\ihasa\OneDrive\Desktop\db2'
    file = os.listdir(path)
    print("--SALAM")
    data = []
    temp = []
    for i in file:
        if i.endswith(".txt"):
            opening = open(i, "r", encoding = "utf-8")
            reading = opening.read()
            f = reading.replace("\n", " ")
            #Tokenization
            #Iterating through each sentence in the file 
            for i in sent_tokenize(f): 
                #Tokenizing the sentence into words 
                for j in word_tokenize(i): 
                    temp.append(j.lower())
                data.append(temp)
