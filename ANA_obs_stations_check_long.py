import requests
from bs4 import BeautifulSoup

DataInicio = '01/01/1900'
DataFim = '11/18/2018'

cod_list=[2346446]
i=0
gages_flow = []
while i < len(cod_list):

    url = 'http://telemetriaws1.ana.gov.br/ServiceANA.asmx/DadosHidrometeorologicos?codEstacao=' + str(cod_list[i]) + '&DataInicio=' + DataInicio + '&DataFim=' + DataFim
    response = requests.get(url)

    try:
        soup = BeautifulSoup(response.content, "xml")
        values = soup.find_all('Vazao')
        if values:
            flows = []
            for value in values:
                flows.append(str(value.get_text()))
            if flows[1]:
                gages_flow.append(str(cod_list[i]))
                print gages_flow
        # else:
        #     print(str(cod_list[i])+": nodata")
    except:
        print("error")

    i+=1
    print i

print("!!!!!!!!!!!!!!!finished!!!!!!!!!!!!!!!")
print gages_flow







