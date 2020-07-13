import re
import string


def parse(file):
    with open(file, 'r') as file:
        data = file.read().split('\n\n')
        is_string_re = 'nif:isString.*\"(.*)\"'
        anchorOf_re = 'nif:anchorOf.*\"(.*)\"'
        has_property = 'itsrdf:taClassRef.*dbo:(.*);'
        in_dbpedia = 'itsrdf:taIdentRef.*dbr:(.*).'
        lastKnowObj = ""

        all_obj = []
        meta = {}
        sentences = {}
        entityPlusRelation = {}
        dbpediaNames = []

        for item in data:
            tmp = re.search(is_string_re, item)
            if tmp:
                sentences[tmp.group(1)] = item

            tmp = re.search(anchorOf_re, item)
            if tmp:
                lastKnowObj = tmp.group(1)
                all_obj.append(tmp.group(1))
                meta[tmp.group(1)] = item

            tmp = re.search(has_property, item)
            if tmp:
                entityPlusRelation[lastKnowObj] = tmp.group(1)[:-1]

            tmp = re.search(in_dbpedia, item)
            if tmp:
                dbpediaNames.append(tmp.group(1)[:-1])

    return sentences, meta, entityPlusRelation, all_obj, dbpediaNames

def parse_odp(file):
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

                if x3[1] == 'locatedinarea':
                    x3[1] = 'location'
                results.append(tuple(x3))

        return results