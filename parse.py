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
