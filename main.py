from click._compat import raw_input
import re

import GetDBPediaInfo
import NLpreprocessing
from knowledgeBase import giveTripleFromKnowledge
from parse import parse


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

    print('\n\n===============================\n\n')

    print('Keanu_Reeves + Texas')
    getinfo = GetDBPediaInfo.getItAllDone('Keanu_Reeves')
    getinfo2 = GetDBPediaInfo.getItAllDone('Texas')
    print(getinfo)
    print(getinfo2)
    print('------------------------------')

    for word1 in getinfo:
        for word2 in getinfo2:
            giveTripleFromKnowledge(word1, word2)


def example2(filename):
    parsed = parse(filename)
    print('Parsed sentences: ', parsed[0])
    print('Parsed objects: ', parsed[1])
    print('Objects + types: ', parsed[2])


if __name__ == '__main__':
    example2('file_100.ttl')
