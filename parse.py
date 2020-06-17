import re


def parse(file):
    with open(file, 'r') as file:
        data = file.read().split('\n\n')
        is_string_re = 'nif:isString.*\"(.*)\"'
        anchorOf_re = 'nif:anchorOf.*\"(.*)\"'
        has_property = 'itsrdf:taClassRef.*dbo:(.*);'

        lastKnowObj = ""
        meta = {}
        sentences = {}
        entityPlusRelation = {}

        for item in data:
            tmp = re.search(is_string_re, item)
            if tmp:
                sentences[tmp.group(1)] = item

            tmp = re.search(anchorOf_re, item)
            if tmp:
                lastKnowObj = tmp.group(1)
                meta[tmp.group(1)] = item

            tmp = re.search(has_property, item)
            if tmp:
                entityPlusRelation[lastKnowObj] = tmp.group(1)

    return sentences, meta, entityPlusRelation