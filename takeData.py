import requests
import unicodedata
import dbConnectSQL as db
# import mysql.connector

class TakeData(db.DbConnectSQL):
    def __init__(self, myURL) -> None:
        super().__init__()
        self.url = myURL
        self.insertingData =[]
        self.data = None
        # r = requests.get(self.url, headers={'content-type': 'application/json; charset=UTF-8'})
        
    def sentRequest(self):
        r = requests.get(self.url)
        print(r.ok)
        if r.ok: 
            self.data = r.json()
            print(len(self.data['quotas']))
            return True
        else: return False
            
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
        with open("myfile.txt", "w") as file1:
            for line in self.insertingData:
                delim = ";"
                res = delim.join([str(ele) for ele in line])
                res = res + "\n"
                print(res)
                file1.writelines(res)
        
        
 
        
        