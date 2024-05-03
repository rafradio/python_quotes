import sys
import requests
import csv

def addreses():
    data = []
    with open('dataCoor2.csv', encoding="utf-8-sig", mode ='r') as f:
        csvFile = csv.reader(f, delimiter  = ';', quotechar=None)
        for lines in csvFile:
            print(lines)
            data.append(lines)
        # data = [line.rstrip().split(";") for line in csvFile]
    return data

def fetch_coordinates(args, addresesList):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    with open("configYandex.txt") as f:
        rawdata = [line.rstrip() for line in f]
    apikey = rawdata[0]
    coordinates = []
    for addr in addresesList:
        r = requests.get(base_url, params={
            "geocode": addr[1],
            "apikey": apikey,
            "format": "json",
        })
        if r.ok: 
            data = r.json()
            # print(data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'].keys())
            print(data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][2])
            # coordinates.append((addr[0], data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']))
            coordinates.append((addr[0], data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][2]))
            
    with open("coordinares1.txt" , encoding="utf-8-sig", mode ="w") as file1:
        for line in coordinates:
            file1.writelines(line[0] + "; " + line[1]['name'] + "\n")
            
    
if __name__ == "__main__":
    addresesList = addreses()
    address = "Россия, Тверская обл., Западная Двина г., Кирова ул."
    print(len(addresesList))
    print(addresesList[0])
    fetch_coordinates(sys.argv, addresesList)