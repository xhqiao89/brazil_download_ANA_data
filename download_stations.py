import requests
import json
import csv

i = 0
while i <22000:
    stations_url = 'http://www.snirh.gov.br/arcgis/rest/services/SGH/REDE_HIDROMETEOROLOGICA_NACIONAL_2018/MapServer/0/query?where=FID>{FID_count}&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=FID%2C+C%C3%B3digo%2C+Tipo%2C+Esta%C3%A7%C3%A3o%2C+Bacia%2C+Rio&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&having=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&queryByDistance=&returnExtentOnly=false&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&f=pjson'.format(FID_count = i)
    print(stations_url)
    r = requests.get(stations_url)
    parsed_r = json.loads(r.text)
    stations_data = parsed_r["features"]

    csv_path = open('C:\QXH\Dissertation\COSMO\stationdata\stations_brazil.csv', 'ab+')
    f = csv.writer(csv_path)
    j = 0
    while j < len(stations_data):
        f.writerow(stations_data[j].values())
        j+=1

    csv_path.close()

    i+=1000