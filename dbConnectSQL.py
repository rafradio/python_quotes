import mysql.connector

class DbConnectSQL:
    def __init__(self) -> None:
        with open("config.txt") as f:
            rawdata = [line.rstrip() for line in f]
        self.mydb = mysql.connector.connect(
            host=rawdata[0],
            user=rawdata[1],
            password=rawdata[2],
            database=rawdata[3]
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("SHOW DATABASES")
        for x in self.mycursor:
            print(x)
        
    def makeSQLInsert(self, data):
        print(len(data))
        sql = "INSERT INTO folkmaik_quota.quotas (link, title, prj_id, user_id) VALUES (%s, %s, %s, %s)"
        self.mycursor.executemany(sql, data)
        # self.mycursor.l
        
        # for line in data:
        #     values = (int(line[0]), str(line[1]),int(line[2]) ,int(line[3]))
        #     self.mycursor.execute(sql, values)
            
        
        self.mydb.commit()
        # print(self.mycursor.fetchall, "record inserted.")
        print(self.mycursor.rowcount, "record inserted.")
        
    def checkSQLUsers(self, data):
        resData = []
        for u in data:  
            val = "%" + str(u) + "%"
            sql = "SELECT id FROM users WHERE email LIKE '" + val + "'"
            self.mycursor.execute(sql)
            rowdata = self.mycursor.fetchall()
            # print(len(rowdata))
            if len(rowdata) == 0:
                sql = "SELECT id FROM users WHERE users.name LIKE '" + val + "'"
                self.mycursor.execute(sql)
                row = [item[0] for item in self.mycursor.fetchall()]
            else:
                row = [item[0] for item in rowdata]
            resData.append(row)
        print("Печатаем данные в колличестве - ", len(resData))
        for el in [str(x) for xs in resData for x in xs]: print(el)
        return resData
        