# Actually usefull

from SPARQLWrapper import SPARQLWrapper, JSON
from knowledgeBase import isInKnowledge

def printResult(results):
    for result in results["results"]["bindings"]:
        print(result["type"]["value"])


def resultToList(results):
    res = []
    for result in results["results"]["bindings"]:
        temp = result["type"]["value"]
        res.append(temp)
    return res


def filterAnswear(dict):
    for x in dict["results"]["bindings"]:
        temp = str(x["type"]["value"])
        x["type"]["value"] = temp[temp.rfind('/') + 1:]
    return dict


def getTypes(object):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    querry = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    PREFIX dbo: <http://dbpedia.org/ontology/>

    SELECT ?type 
    WHERE { <http://dbpedia.org/resource/"""
    querry += object
    querry += """> rdf:type ?type 
    FILTER ( strstarts(str(?type), "http://dbpedia.org/ontology/" ) ) }"""

    sparql.setQuery(querry)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results


def filterUsefullTypes(listOfTypes):
    for type in listOfTypes:
        if (not isInKnowledge(type)):
            listOfTypes.remove(type)


def getItAllDone(object):
    result = getTypes(object)
    result = filterAnswear(result)
    result = resultToList(result)
    filterUsefullTypes(result)
    return result


if __name__ == '__main__':
    # results = getTypes('Microsoft')
    # for result in results["results"]["bindings"]:
    #     print(result["type"]["value"])
    #
    # print('\n\n')
    #
    # resultFiltered = filterAnswear(results)
    # for result in resultFiltered["results"]["bindings"]:
    #     print(result["type"]["value"])
    res = getItAllDone('Microsoft')
    print(res)
    # printResult(res)