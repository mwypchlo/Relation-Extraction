import GetDBPediaInfo

getinfo = GetDBPediaInfo.getTypes('Bill_Gates')

if __name__ == '__main__':
    GetDBPediaInfo.printResult(getinfo)
    processedInfo = GetDBPediaInfo.filterAnswear(getinfo)
    GetDBPediaInfo.printResult(processedInfo)
