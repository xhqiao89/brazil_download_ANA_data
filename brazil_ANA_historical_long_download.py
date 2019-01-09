import requests
import BeautifulSoup
import csv
import datetime as dt
import calendar

DataInicio = '01/01/1980'
DataFim = '01/01/2019'

cod_list=[61834000]
i=0
while i < len(cod_list):

    url = 'http://telemetriaws1.ana.gov.br/ServiceANA.asmx/HidroSerieHistorica?codEstacao=' + str(cod_list[i]) + '&dataInicio=' + DataInicio + '&dataFim=' + DataFim + '&tipoDados=3&nivelConsistencia=1'
    response = requests.get(url)

    try:
        soup = BeautifulSoup(response.content, "xml")

        value01 = soup.find_all('Vazao01')
        value02 = soup.find_all('Vazao02')
        value03 = soup.find_all('Vazao03')
        value04 = soup.find_all('Vazao04')
        value05 = soup.find_all('Vazao05')
        value06 = soup.find_all('Vazao06')
        value07 = soup.find_all('Vazao07')
        value08 = soup.find_all('Vazao08')
        value09 = soup.find_all('Vazao09')
        value10 = soup.find_all('Vazao10')
        value11 = soup.find_all('Vazao11')
        value12 = soup.find_all('Vazao12')
        value13 = soup.find_all('Vazao13')
        value14 = soup.find_all('Vazao14')
        value15 = soup.find_all('Vazao15')
        value16 = soup.find_all('Vazao16')
        value17 = soup.find_all('Vazao17')
        value18 = soup.find_all('Vazao18')
        value19 = soup.find_all('Vazao19')
        value20 = soup.find_all('Vazao20')
        value21 = soup.find_all('Vazao21')
        value22 = soup.find_all('Vazao22')
        value23 = soup.find_all('Vazao23')
        value24 = soup.find_all('Vazao24')
        value25 = soup.find_all('Vazao25')
        value26 = soup.find_all('Vazao26')
        value27 = soup.find_all('Vazao27')
        value28 = soup.find_all('Vazao28')
        value29 = soup.find_all('Vazao29')
        value30 = soup.find_all('Vazao30')
        value31 = soup.find_all('Vazao31')
        times = soup.find_all('DataHora')

        dates = []
        flows = []

        for time in times:
            time_a = dt.datetime.strptime(time.get_text().strip(), "%Y-%m-%d %H:%M:%S")
            year_a = time_a.year
            month_a = time_a.month
            for k in range(1,32):
                dates.append(dt.datetime(year_a,month_a,k, 0, 0, 0))
            print dates

        j=0
        while j < len(value01):
            flows.append(value01[j].get_text().strip())
            flows.append(value02[j].get_text().strip())
            flows.append(value03[j].get_text().strip())
            flows.append(value04[j].get_text().strip())
            flows.append(value05[j].get_text().strip())
            flows.append(value06[j].get_text().strip())
            flows.append(value07[j].get_text().strip())
            flows.append(value08[j].get_text().strip())
            flows.append(value09[j].get_text().strip())
            flows.append(value10[j].get_text().strip())
            flows.append(value11[j].get_text().strip())
            flows.append(value12[j].get_text().strip())
            flows.append(value13[j].get_text().strip())
            flows.append(value14[j].get_text().strip())
            flows.append(value15[j].get_text().strip())
            flows.append(value16[j].get_text().strip())
            flows.append(value17[j].get_text().strip())
            flows.append(value18[j].get_text().strip())
            flows.append(value19[j].get_text().strip())
            flows.append(value20[j].get_text().strip())
            flows.append(value21[j].get_text().strip())
            flows.append(value22[j].get_text().strip())
            flows.append(value23[j].get_text().strip())
            flows.append(value24[j].get_text().strip())
            flows.append(value25[j].get_text().strip())
            flows.append(value26[j].get_text().strip())
            flows.append(value27[j].get_text().strip())
            flows.append(value28[j].get_text().strip())
            flows.append(value29[j].get_text().strip())
            flows.append(value30[j].get_text().strip())
            flows.append(value31[j].get_text().strip())
            j+=1

        flows_new= flows[::-1]
        dates_new = dates[::-1]

        csv_path = '/home/sherry/Brazil_historical_data/Long/{filename}.csv'.format(filename = str(cod_list[i]))
        csv_file = open(csv_path, 'wb')
        f = csv.writer(csv_file)
        vl=0
        while vl < len(flows):
            flow_date_array = [dates_new[vl], flows_new[vl]]
            f.writerow(flow_date_array)
            vl+=1
        csv_file.close()

    except:
        print("error")

    i+=1
    print i

print("!!!!!!!!!!!!!!!finished!!!!!!!!!!!!!!!")







