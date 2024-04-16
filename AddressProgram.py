import sys
import re

def main(args):
    with open('addresProgram.txt', encoding="utf-8") as f:
        data = [line.rstrip().replace('"', '') for line in f]
    index = 1
    for str in data:
        if str.rfind("@") > -1:
            allIndexes = [i for i, ltr in enumerate(str) if ltr == "@"]
            if len(allIndexes) > 1:
                attempt = 1
                while attempt < len(allIndexes):
                    subStr = str[allIndexes[attempt -1]:allIndexes[attempt]]
                    if subStr.rfind(";") == -1: print(index, allIndexes)
                    attempt += 1
                
        index += 1
    index = 1
    
    for str in data:
        if str.rfind("@") > -1:
            str = str.replace('"', '')
            addreses = str.split(";")
            for adr in addreses:
                adr = adr.strip()
                
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                match = re.match(regex, adr)
                if match == None:
                    print('Bad Syntax - ', index, adr)
                    
        index += 1
        
        

if __name__ == "__main__":
    main(sys.argv)
    