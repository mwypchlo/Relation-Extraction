from click._compat import raw_input
import re

import GetDBPediaInfo
import NLpreprocessing

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

if __name__ == '__main__':
    getinfo = GetDBPediaInfo.getTypes('Bill_Gates')
    getinfo2 = GetDBPediaInfo.getTypes('Microsoft')
    processedInfo1 = GetDBPediaInfo.filterAnswear(getinfo)
    processedInfo2 = GetDBPediaInfo.filterAnswear(getinfo2)
    GetDBPediaInfo.printResult(processedInfo1)
    print("-------------------------------------------------")
    GetDBPediaInfo.printResult(processedInfo2)
