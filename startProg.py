import sys
import takeData
# import dbConnectSQL
import createDataFromFile as create

def main(args):
    projectId, users, myURL = create.createData(args[1])
    print("start - ", projectId, users)
    dt = takeData.TakeData(myURL)
    # dBase = dbConnectSQL.DbConnectSQL()
    if dt.sentRequest(): 
        print(dt.data)
        dt.createData(projectId, users)

        print(dt.insertingData)
        print(len(dt.insertingData))
        dt.makeSQLInsert(dt.insertingData)
    else: print("Данных в запросе нет")
    # dBase.makeSQLInsert(dt.insertingData)

if __name__ == "__main__":
    main(sys.argv)
    