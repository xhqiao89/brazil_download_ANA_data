import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import datetime as dt

today = dt.date.today()
day = today.day
first = today.replace(day=1)
month = first - dt.timedelta(days=1)
lastmonth = month.replace(day=day)

codEstacao = '64618500'
DataInicio = '21/8/2018'
DataFim = '28/8/2018'

url = 'http://telemetriaws1.ana.gov.br/ServiceANA.asmx/DadosHidrometeorologicos?codEstacao=' + codEstacao + '&DataInicio=' + DataInicio + '&DataFim=' + DataFim

response = requests.get(url)

soup = BeautifulSoup(response.content, "xml")

times = soup.find_all('DataHora')
values = soup.find_all('Vazao')

dates = []
flows = []

for time in times:
    dates.append(dt.datetime.strptime(time.get_text().strip(), "%Y-%m-%d %H:%M:%S"))

for value in values:
    flows.append(value.get_text().strip())

flows_new= flows[::-1]
dates_new = dates[::-1]
print flows_new
print dates_new

plt.plot(dates_new,flows_new)
plt.show()