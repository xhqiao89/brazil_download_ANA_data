import requests
from bs4 import BeautifulSoup
import csv
import datetime as dt

DataInicio = '01/01/1980'
DataFim = '01/01/2019'

cod_list=[61834000,74800000]
i=0
while i < len(cod_list):

    url = 'http://telemetriaws1.ana.gov.br/ServiceANA.asmx/HidroSerieHistorica?codEstacao=' + str(cod_list[i]) + '&dataInicio=' + DataInicio + '&dataFim=' + DataFim + '&tipoDados=3&nivelConsistencia=1'
    response = requests.get(url)

    try:
        soup = BeautifulSoup(response.content, "xml")
        values = soup.find_all('Vazao01')
        times = soup.find_all('DataHora')
        print values

        dates = []
        flows = []

        for time in times:
            dates.append(dt.datetime.strptime(time.get_text().strip(), "%Y-%m-%d %H:%M:%S"))

        for value in values:
            flows.append(value.get_text().strip())

        flows_new= flows[::-1]
        dates_new = dates[::-1]

        csv_path = '/home/sherry/Brazil_historical_data/Long/{filename}.csv'.format(filename = str(cod_list[i]))
        csv_file = open(csv_path, 'wb')
        f = csv.writer(csv_file)
        j=0
        while j < len(flows):
            flow_date_array = [dates_new[j], flows_new[j]]
            f.writerow(flow_date_array)
            j+=1
        csv_file.close()
        #
        #     if flows[1]:
        #         gages_with_flow.append(str(cod_list[i]))
        #         print gages_with_flow
    # else:
    #     print(str(cod_list[i])+": nodata")
    except:
        print("error")

    i+=1
    print i

print("!!!!!!!!!!!!!!!finished!!!!!!!!!!!!!!!")







