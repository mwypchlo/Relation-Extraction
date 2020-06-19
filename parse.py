import re


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