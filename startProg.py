import sys
import takeData
# import dbConnectSQL
import createDataFromFile as create

def main(args):
    projectId, users, myURL = create.createData(args[1])
    print("start - ", projectId, users)
    dt = takeData.TakeData(myURL)
    # dBase = dbConnectSQL.DbConnectSQL()
    
    # dt.takeKeys()
    dt.createData(projectId, users)
    # dt.checkData()
    # dt.insertData()
    # dt.writeToFile()
    # dt.makeSQLInsert()
    print(dt.insertingData)
    print(len(dt.insertingData))
    # print(dt.mydb)
    dt.makeSQLInsert(dt.insertingData)
    # dBase.makeSQLInsert(dt.insertingData)

if __name__ == "__main__":
    main(sys.argv)
    