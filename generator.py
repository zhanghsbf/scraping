from io import StringIO
from random import randint
import re
import os

def openFile():
    with open("model/孔乙己.txt",'rb') as file:
        text = file.read()                          # txt是unicode码，用二进制读取，读成字符串，在用utf-8解码
    return text.decode('utf-8')

def cleanText(text):

    text = text.replace("\n"," ")
    # text = text.replace(" ", "")
    # text = re.sub("(\\\\u)","", text)
    textList = []
    for i in range(0,len(text)):
        textList.append(text[i])

    return textList
    # textList = [i for i in text if i != ""]
    # textList = filter(lambda x:x.isalpha() or x in ("，","。","？","！","：","-","“","”"), textList)
    # for i in textList:
    #     print(i,end=" ")
def getWordDict(textList):                  # 默认两个字一个词，找出每个字所有能构成的词
    wordDict = {}
    for i in range(1,len(textList)):
        if textList[i-1] not in wordDict:
            wordDict[textList[i-1]] = {}    # 首个字，value里跟个子级字典，放第二个字
            x = wordDict[textList[i-1]]
        if textList[i] not in x:
            x[textList[i]] = 1              # 第二个字，value为计数器
            y = x[textList[i]]
        y +=1
    # print(wordDict)
    return wordDict

def countWords(wordList):               # 统计首个字构成的词出现的总次数
    sum = 0
    for i in wordList.values():
        sum += i
    return sum

def getRandomWord(wordList):
    randIndex = randint(1,countWords(wordList))    # 得到1-总次数之间的一个随机数，相当于随机抽一个词，频率大的几率高
    for key,value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return key
def mk_txt(chain):
    with open("随机文本.txt","a") as new_txt:
        new_txt.write(chain+"\n")
def createChain(length,first_word="孔"):
    wordDict = getWordDict(cleanText(openFile()))
    print(wordDict["孔"])
    chain = ""
    current = first_word
    for i in range(length):
        chain += current
        current = getRandomWord(wordDict[current])
    mk_txt(chain)
    print(chain)

createChain(100)

