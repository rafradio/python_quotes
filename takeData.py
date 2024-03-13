import requests
import unicodedata
import dbConnectSQL as db
# import mysql.connector

class TakeData(db.DbConnectSQL):
    def __init__(self, myURL) -> None:
        super().__init__()
        self.url = myURL
        self.insertingData =[]
        # self.url = "https://api.alchemer.com/v5/survey/7740515/quotas?api_token=59907c039d7a83a104f6623e125381a64bc6614dd55618be5d&api_token_secret=A9m4.LEiwlUjM"
        # r = requests.get(self.url, headers={'content-type': 'application/json; charset=UTF-8'})
        r = requests.get(self.url)
        self.data = r.json()
        # print(self.data)
        print(len(self.data['quotas']))
        print(type(self.data['quotas'][3]))
            
    def createData(self, projectId, users):
        for user in users:
            for line in self.data['quotas']:
                # string = unicodedata.normalize("NFKD", line['name'])
                string = line['name'].replace(u'\xa0', u'')
                newLine = (line['id'], string, projectId, user)
                self.insertingData.append(newLine)
                
    def checkData(self):
        i = len(self.insertingData)
        print("Длина - ", i)    
        
    def writeToFile(self):
        # for line in self.insertingData:
        #     delim = ";"
        #     res = delim.join([str(ele) for ele in line])
        #     print(res)
        with open("myfile.txt", "w") as file1:
            for line in self.insertingData:
                delim = ";"
                res = delim.join([str(ele) for ele in line])
                res = res + "\n"
                print(res)
                file1.writelines(res)
        
        
 
        
        