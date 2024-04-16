import sys

def main(args):
    with open('addresProgram.txt', encoding="utf-8") as f:
        data = [line.rstrip() for line in f]
    index = 1
    for str in data:
        if str.rfind("@") > -1:
            allIndexes = [i for i, ltr in enumerate(str) if ltr == "@"]
            if len(allIndexes) > 1:
                attempt = 1
                while attempt < len(allIndexes):
                    sBegin = attempt -1
                    sEnd = attempt
                    subStr = str[allIndexes[sBegin]:allIndexes[sEnd]]
                    if subStr.rfind(";") == -1: print(index, allIndexes)
                    attempt += 1
                
        index += 1
        

if __name__ == "__main__":
    main(sys.argv)
    