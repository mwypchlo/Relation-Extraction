from SPARQLWrapper import SPARQLWrapper, JSON

def printResult(results):
    for result in results["results"]["bindings"]:
        print(result["type"]["value"])


def filterAnswear(dict):
    for x in dict["results"]["bindings"]:
        temp = str(x["type"]["value"])
        # temp = temp[temp.rfind('/') + 1:]
        # print(temp)
        # print(temp[temp.rfind('/')+1:])
        x["type"]["value"] = temp[temp.rfind('/') + 1:]

    return dict


def getTypes(object):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    querry = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    SELECT ?type 
    WHERE { <http://dbpedia.org/resource/"""
    querry += object
    querry += "> rdf:type ?type}"

    sparql.setQuery(querry)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results


if __name__ == '__main__':
    results = getTypes('Microsoft')
    for result in results["results"]["bindings"]:
        print(result["type"]["value"])

    print('\n\n')

    resultFiltered = filterAnswear(results)
    for result in resultFiltered["results"]["bindings"]:
        print(result["type"]["value"])