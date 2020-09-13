import re
import string
from pathlib import Path
import GetDBPediaInfo

def parse(file):
    # file = Path("Training Data/" + file)
    with open(file, 'r') as file:
        data = file.read().split('\n\n')
        is_string_re = 'nif:isString.*\"(.*)\"'
        anchorOf_re = 'nif:anchorOf.*\"(.*)\"'
        has_property = 'itsrdf:taClassRef.*dbo:(.*);'
        # in_dbpedia = 'itsrdf:taIdentRef.*(.*).'
        in_dbpedia = 'itsrdf:taIdentRef.*dbr:(.*).'
        in_dbpedia2 = 'itsrdf:taIdentRef.*<http://dbpedia.org/resource/(.*). '
        lastKnowObj = ""

        all_obj = []
        meta = {}
        sentences = {}
        entityPlusRelation = {}
        dbpediaNames = {}

        for item in data:
            tmp = re.search(is_string_re, item)
            if tmp:
                sentences[tmp.group(1)] = item

            tmp = re.search(anchorOf_re, item)
            if tmp:
                # print('anchorOfRe: ', tmp.group(1))
                lastKnowObj = tmp.group(1)
                all_obj.append(tmp.group(1))
                meta[tmp.group(1)] = item

            tmp = re.search(has_property, item)
            if tmp:
                # print('has_property: ',tmp.group(1))
                entityPlusRelation[lastKnowObj] = tmp.group(1)[:-1]

            tmp = re.search(in_dbpedia, item)
            if not tmp:
                tmp = re.search(in_dbpedia2, item)
            if tmp:
                if tmp.group(1).endswith(' '):
                    dbpediaNames[lastKnowObj] = tmp.group(1)[:-1]

                else:
                    dbpediaNames[lastKnowObj] = tmp.group(1)

    allInfo = {}
    for key, value in entityPlusRelation.items():
        if key in dbpediaNames.keys():
            # print(dbpediaNames[key])
            temp = GetDBPediaInfo.getItAllDone(dbpediaNames[key])
            if value not in temp:
                temp.append(value)
            allInfo[key] = temp

    # print('\nentityPlusRelation: ', entityPlusRelation)
    # print('\ndbpediaNames: ',dbpediaNames)
    # print('\nall_info: ',allInfo)

    # not returning meta, all_obj, dbpediaNames, entityPlusRelation - useless in main
    return sentences, allInfo

def parse_answer(file):
    with open(file, 'r') as file:
        data = file.read().split('\n\n')

        results = []
        for item in data:
            if item[:3] == '[ a' and item[-3:] == '] .':
                x3 = []
                for fi in item.split('\n')[1:4]:
                    aa = fi.split(':')[2]

                    if aa[:2] == '//' and aa[-3:] == '> ;':
                        aa = aa.split('/')[-1].split('(')[0]
                    else:
                        aa = aa[:-2]

                    aa = aa.replace('_', '').replace('%2C', '').lower()
                    aa = aa.translate(str.maketrans('', '', string.punctuation))
                    aa = aa.strip()
                    x3.append(aa)

                results.append(tuple(x3))

        return results

def answer_print(file): #wypisz pierwsza relacje
    a = parse_answer(file)
    print('------------------------')
    print('rdf:object')
    print(a[0][0])
    print('------------------------')
    print('rdf:predicate')
    print(a[0][1])
    print('------------------------')
    print('rdf:subject')
    print(a[0][2])
