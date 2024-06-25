import pandas as pd
import openpyxl
import time

start = time.time()
dataframe = openpyxl.load_workbook("testxls.xlsm")

dataframe1 = dataframe.active
mydata = []
dataset = []

for row in range(0, dataframe1.max_row):
    mydata.append([col[row].value for col in dataframe1.iter_cols(1, dataframe1.max_column)])

for i in range(len(mydata[0])):
    dataset.append([mydata[j][i] for j in range(len(mydata))])

    
# print(mydata[4])
# print(dataset[0][4].replace("megafon\\","").rstrip() + "@megafon.ru")
# print(dataset[4][0])

for i in range(len(dataset)-1):
    # checkSet = []
    s = set(dataset[i])
    for el in s:
        str1 = str(el).replace("megafon\\","").rstrip() + "@megafon.ru"
        checkSet = list(filter(lambda x: str(x).find(str1) != -1, dataset[4]))
        if len(checkSet) > 0: print(el)
    # for j in range(len(dataset[i])):
    #     str1 = str(dataset[i][j]).replace("megafon\\","").rstrip() + "@megafon.ru"
    #     checkSet = list(filter(lambda x: str(x).find(str1) != -1, dataset[4]))
    #     if len(checkSet) > 0: print(str1, j)
        
end = time.time()
print("The time : ",round(end - start,5))