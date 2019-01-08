import requests
import BeautifulSoup
import csv

DataInicio = '01/01/1980'
DataFim = '01/01/2019'

cod_list=[61834000,74800000]
i=0
gages_with_flow = []
while i < len(cod_list):

    url = 'http://telemetriaws1.ana.gov.br/ServiceANA.asmx/HidroSerieHistorica?codEstacao=' + str(cod_list[i]) + '&dataInicio=' + DataInicio + '&dataFim=' + DataFim + '&tipoDados=1&nivelConsistencia=1'
    response = requests.get(url)

    try:
        soup = BeautifulSoup(response.content, "xml")
        values = soup.find_all('Vazao')
        print values
        if values:
            flows = []
            for value in values:
                flows.append(str(value.get_text()))

            csv_path = 'C:\QXH\Dissertation\COSMO\stationdata\H\{filename}.csv'.format(filename = str(cod_list[i]))
            csv_file = open(csv_path, 'wb')
            f = csv.writer(csv_file)
            f.writerow(flows)
            csv_path.close()

            if flows[1]:
                gages_with_flow.append(str(cod_list[i]))
                print gages_with_flow
    # else:
    #     print(str(cod_list[i])+": nodata")
    except:
        print("error")

    i+=1
    print i

print("!!!!!!!!!!!!!!!finished!!!!!!!!!!!!!!!")
print gages_with_flow







