from click._compat import raw_input
import re

import GetDBPediaInfo
import NLpreprocessing
from knowledgeBase import giveTripleFromKnowledge, giveTripleFromKnowledgeNoDoubleCheck
from parse import parse, parseSentence


# getinfo = GetDBPediaInfo.getTypes('Bill_Gates')

# if __name__ == '__main__':
#     text = raw_input("Write the sentence: ")
#     nl_data = NLpreprocessing.get_continuous_chunks(text)
#     print(nl_data)
#     for p in nl_data:
#         s = p.replace(" ", "_")
#         print(s)
#         GetDBPediaInfo.printResult(GetDBPediaInfo.getTypes(s))
#         processedInfo = GetDBPediaInfo.filterAnswear(GetDBPediaInfo.getTypes(s))
#         GetDBPediaInfo.printResult(processedInfo)
#         print("------------------------------------------------------------------------------------")


def example1():
    print('Bill Gates + Microsoft')
    getinfo = GetDBPediaInfo.getItAllDone('Bill_Gates')
    getinfo2 = GetDBPediaInfo.getItAllDone('Microsoft')
    print(getinfo)
    print(getinfo2)
    print('------------------------------')

    for word1 in getinfo:
        for word2 in getinfo2:
            giveTripleFromKnowledge(word1, word2)

    print('\n===============================\n')

    print('Keanu_Reeves + Texas')
    getinfo = GetDBPediaInfo.getItAllDone('Keanu_Reeves')
    getinfo2 = GetDBPediaInfo.getItAllDone('Texas')
    print(getinfo)
    print(getinfo2)
    print('------------------------------')

    for word1 in getinfo:
        for word2 in getinfo2:
            # print('-------------------\n', word1, word2, sep=' <-> ')
            giveTripleFromKnowledge(word1, word2)



def example2(filename):
    parsed = parse(filename)
    print('Parsed sentences: ', parsed[0])
    print('Parsed objects: ', parsed[1])
    print('Objects + types: ', parsed[2])
    print('\n')
    # print(parsed[3])

    listt = []
    for object in parsed[3]:
        temp = []
        temp.append(parsed[2][object])
        listt.append(temp)


    for word1 in listt[0]:
        for word2 in listt[1]:
            print('-------------------\n', word1, '<-> ', word2)
            giveTripleFromKnowledgeNoDoubleCheck(word1, word2)


def example3(filename):
    parsed = parse(filename)
    print('Parsed sentences: ', parsed[0])
    print('Parsed objects: ', parsed[1])
    print('Objects + types: ', parsed[2])
    print('\n')
    # print(parsed[3])

    print(parsed[4])

    data = []
    for objs in parsed[4]:
        temp = GetDBPediaInfo.getItAllDone(objs)
        print(temp)
        data.append(temp)

    print('\n')

    for word1 in data[0]:
        for word2 in data[1]:
            # print('-------------------\n', word1, word2, sep=' <-> ')
            giveTripleFromKnowledge(word1, word2)

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
    print('Parsed objects: ', data1)

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
    #example1()                # Getting data from DBpedia
    #example2('file_100.ttl')  # Working parser
    #example3('file_100.ttl')    # Parser + DBpedia
    text = raw_input("Type 1 to read data from file or type 2 to write your own sentence: ")
    if text=='1':
        text2=raw_input("Provide file name(path): ")
        example3(text2)
    if text=='2':
        text2 = raw_input("Write your own sentence: ")
        getInfoFromSentence(text2)

