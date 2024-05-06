import sys
import re
import csv

def checkNewLine(args):
    data = []
    with open('addresProgram1.csv', mode ='r') as f:
        # csvFile = csv.reader(f, quotechar=None)
        csvFile = csv.reader(f, delimiter  = ';', quotechar=None)
        for lines in csvFile:
            # print(lines)
            data.append(lines)
           
    index = 1        
    for arr in data:
        if arr[0].rfind("@") > -1: print(arr, index)
        index += 1

def main(args):  
    with open('addresProgram.txt', encoding="utf-8") as f:
        data = [line.rstrip().replace('"', '') for line in f]
    
    
    
    index = 1
    for str in data:
        # str = stringMy[1].rstrip().replace("\\r\\n", "")
        # str = str.replace('"', '')
        if str.rfind("@") > -1:
            allIndexes = [i for i, ltr in enumerate(str) if ltr == "@"]
            if len(allIndexes) > 1:
                attempt = 1
                while attempt < len(allIndexes):
                    subStr = str[allIndexes[attempt -1]:allIndexes[attempt]]
                    if subStr.rfind(";") == -1: print(index, allIndexes)
                    attempt += 1
                
        index += 1
    checkEmailSpelling(data)
        
def checkEmailSpelling(data):
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
    # checkNewLine(sys.argv)
    main(sys.argv)
    