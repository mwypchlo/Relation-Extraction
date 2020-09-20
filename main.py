from click._compat import raw_input
import re

import GetDBPediaInfo
import NLpreprocessing
from knowledgeBase import giveTripleFromKnowledge, giveTripleFromKnowledgeNoDoubleCheck
from parse import parse, answer_print


def example3(filename):
    parsed = parse(filename)
    print('Parsed sentences: ', parsed[0].keys())
    print('Parsed objects: ', parsed[1])
    print()
    findRelations(parsed[1])


def findRelations(dictOfEntities):

    dictKeys = list(dictOfEntities.keys())
    firstElement = 0
    endElement = len(dictKeys)

    while firstElement < endElement:
        obj1 = dictOfEntities[dictKeys[firstElement]]
        nextElement = firstElement + 1
        while nextElement < endElement:
            obj2 = dictOfEntities[dictKeys[nextElement]]
            nextElement = nextElement + 1
            print()
            print(dictKeys[firstElement], dictKeys[nextElement - 1], sep=' <-> ')
            for word1 in obj1:
                for word2 in obj2:
                    result = giveTripleFromKnowledge(word1, word2)
                    if result:
                        print(result)
        firstElement = firstElement + 1



def getObjectsFromSentence(text):
    data2=[]
    nl_data = NLpreprocessing.get_continuous_chunks(text)
    for p in nl_data:
        s=p.replace(" ", "_")
        data2.append(s)
    return data2


def getInfoFromSentence(text):
    data1=getObjectsFromSentence(text)
    print('Sentence: ', text)
    print('Objects: ', data1)

    print(data1)

    data = []
    for objs in data1:
        temp = GetDBPediaInfo.getItAllDone(objs)
        print(temp)
        data.append(temp)

    print('\n')

    for word1 in data[0]:
        for word2 in data[1]:
            giveTripleFromKnowledge(word1, word2)


if __name__ == '__main__':

    #example3('file_2.ttl')    # Parser + DBpedia
    #answer_print('file_2.ttl') # answer
     text = raw_input("Type 1 to read data from file or type 2 to write your own sentence: ")
     if text=='1':
         text2=raw_input("Provide file name(path): ")
         example3(text2)
         answer_print(text2)
     if text=='2':
         text2 = raw_input("Write your own sentence: ")
         getInfoFromSentence(text2)



