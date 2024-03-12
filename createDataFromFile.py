import sys

def createData(args):
    with open('data.txt') as f:
        data = [line.rstrip() for line in f]
    
    if args == "1": myURL = data[1][:35] + data[0] + data[1][42:] 
    if args == "2": myURL = data[2][:35] + data[0] + data[2][42:]
    
    return data[3], data[4:], myURL

if __name__ == "__main__":
    projectId, users, myURL = createData(sys.argv)
    print(projectId, users, myURL)