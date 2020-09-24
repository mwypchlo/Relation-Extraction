from click._compat import raw_input
import re

import GetDBPediaInfo
import NLpreprocessing
from knowledgeBase import giveTripleFromKnowledge
from parse import parse, answer_print


def seekRelations(filename):
    parsed = parse(filename)
    # print('Parsed sentences: ', list(parsed[0])[0])
    # print('Parsed objects: ', parsed[1])
    # print()
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

    data = []
    for objs in data1:
        temp = GetDBPediaInfo.getItAllDone(objs)
        print(temp)
        data.append(temp)

    print('\n')

    for word1 in data[0]:
        for word2 in data[1]:
            giveTripleFromKnowledge(word1, word2)

def main_script():
    text = raw_input("Type '1' to read data from file or type '2' to write your own sentence: ")
    if text in('1','2'):
        if text == '1':
            text2 = raw_input("Provide file name(path): ")
            while True:
                text3 = raw_input("Type '1' to display expected triples, type '2' to display found objects, type '3' to display the result of relation extraction or '4' to exit: ")
                if text3 in('1','2', '3','4'):
                    if text3 == '1':
                        answer_print(text2)
                        continue
                    if text3=='2':
                        textparsed = parse(text2)
                        for key in textparsed[0].keys():
                            print('Parseed sentence: ', key)
                        print('\nParsed objects: ')
                        for key, value in textparsed[1].items():
                            buffer = ''
                            for vals in value:
                                buffer = buffer + str(vals) + ', '
                            buffer = buffer[0:-2]
                            print(key, ': ', buffer)
                        continue
                    if text3 =='3':
                        seekRelations(text2)
                        continue
                    if text3 =='4':
                        exit()
                        break
        if text == '2':
            text2 = raw_input("Write your own sentence: ")
            getInfoFromSentence(text2)
    else:
        print('Invalid input')


if __name__ == '__main__':
    while True:
        main_script()
        while True:
            answer = raw_input('Run the program again? (y/n): ')
            if answer in ('y', 'n'):
                break
            print('Invalid input.')
        if answer == 'y':
            continue
        else:
            break
