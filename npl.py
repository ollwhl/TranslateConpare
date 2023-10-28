#!/usr/bin/python3
from os import TMP_MAX
import sys
from tokenize import String
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
deeplP=2 
googleP=1
weliboP=0


def enProces(str):
    str = str.lower()
    words = word_tokenize(str)
    marks = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','《','》']
    words = [word for word in words if word not in marks]
    #del words[0]
    return words
def jpProces(str):
    str=neologdn.normalize(str)
    marks=['[','!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\'','\]','^','_','`','{','|','}','~','「','」','〔','〕','“','”','〈','〉','『','』','【','】','＆','＊','・','（','）','＄','＃','＠','。','、','？','！','｀','＋',' ￥','％',']']
    tagger = MeCab.Tagger("-Owakati") 
    words = tagger.parse(str).split()
    words = [word for word in words if word not in marks]
    return(words)
def getLDR(wList1, wList2):

    if len(wList1) == 0:
        return len(wList2)
    elif len(wList2) == 0:
        return len(wList1)
    elif wList1 == wList2:
        return 0

    if wList1[len(wList1)-1] == wList2[len(wList2)-1]:
        d = 0
    else:
        d = 1
    
    return min(getLDR(wList1, wList2[:-1]) + 1,
                getLDR(wList1[:-1], wList2) + 1,
                getLDR(wList1[:-1], wList2[:-1]) + d)
def Levenshtein_Distance(str1, str2):
    matrix = [[ i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if(str1[i-1] == str2[j-1]):
                d = 0
            else:
                d = 1
            
            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+d)

    return matrix[len(str1)][len(str2)]


def compare(googleLines,deeplLines,weliboLines):
    gd=Levenshtein_Distance(googleLines, deeplLines)
    gw=Levenshtein_Distance(googleLines, weliboLines)
    dw=Levenshtein_Distance(deeplLines, weliboLines)
    if gd > gw:
        finaltext=deeplLines
    elif gw > dw:
        finaltext=googleLines
    else:
        finaltext=deeplLines
    return finaltext

#print("source:",wListSource)
#print("wList1:%d"%len(wList1)+"  wList2:%d"% len(wList2))
#print("Google:",wListG)
#print("DeepL",wListD)
#print("LDR=%d"% getLDR(str1, str2))
#print("google Ld=",Levenshtein_Distance(wListSource, wListG))
#print("deepL Ld=",Levenshtein_Distance(wListSource, wListD))
#print("weilbo Ld=",Levenshtein_Distance(wListSource, wListW))