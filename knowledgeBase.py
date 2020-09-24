knowledge = [ # [DOMAIN, RANGE, PROPERTY]
    ['Organisation', 'Organisation', 'affilation'],
    ['Person', 'EducationalInstitution',  'almaMater'],
    ['Band', 'Person', 'bandMember'],
    ['Person', 'Place', 'birthPlace'],
    ['Organisation', 'Person', 'ceo'],
    ['Person', 'Person', 'child'],
    ['Athlete', 'SportsTeam', 'club'],
    ['Organization', 'Country', 'country'],
    ['Person', 'Country', 'country'],
    ['Place', 'Country', 'country'],
    ['Person', 'Place',  'deathPlace'],
    ['Athlete', 'SportsTeam', 'debutTeam'],
    ['PopulatedPlace', 'PopulatedPlace', 'department'],
    ['Place', 'PopulatedPlace', 'district'],
    ['Scientist', 'Person', 'doctoralAdvisor'],
    ['Scientist', 'Person', 'doctoralStudent'],
    ['Person', 'Organisation', 'employer'],
    ['Band', 'Person', 'formerBandMember'],
    ['Athlete', 'SportsTeam', 'formerTeam'],
    ['Organization', 'City', 'foundationPlace'],
    ['Organization', 'PopulatedPlace', 'headquarter'],
    ['Organization', 'Settlement', 'hometown'],
    ['Person', 'Settlement', 'hometown'],
    ['PopulatedPlace', 'Person', 'leaderName'],
    ['Place', 'Place', 'locatedInArea'],
    ['Person', 'Place', 'location'],
    ['Organization', 'Place', 'location'],
    ['Place', 'Place', 'location'],
    ['Person', 'Country', 'nationality'],
    ['Person', 'Person', 'parent'],
    ['Organization', 'Person', 'president'],
    ['Person', 'Organization', 'president'],
    ['Person', 'Person', 'relative'],
    ['Person', 'Person', 'spouse'],
    ['Company', 'Company', 'subsidiary'],
    ['ArchitecturalStructure', 'Organization', 'tenant'],
    ['Athlete', 'Person', 'trainer']
]


def isInKnowledge(word):
    x = 0
    y = 0
    while x < len(knowledge):
        while y < len(knowledge[x]):
            if (word == knowledge[x][y]):
                return True
            y = y + 1
        x = x + 1
        y = 0
    return False


def giveTripleFromKnowledge(word1, word2):
    result = ''
    for triple in knowledge:
        if word1 == triple[0] and word2 == triple[1]:
            result = result + str(triple)
        else:
            if (word1 == triple[1] and word2 == triple[0]):
                result = result + str(triple)
    return result
