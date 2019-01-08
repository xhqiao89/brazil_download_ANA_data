import requests
from bs4 import BeautifulSoup

DataInicio = '08/08/2018'
DataFim = '08/10/2018'

cod_list=[65260001,65270000,65271000,65275000,65280000,65285000,65293000,65295000,65295001,65299000,65299001,65306000,65307000,65308000,65310000,65310000,65310001,65310500,65320000,65330000,65340000,65350000,65365801,65365810,65370001,65415000,65415001,65420003,65420004,65480000,65550050,65687000,65764001,65769500,65771000,65774400,65774408,65775901,65803001,65808500,65809000,65812000,65813000,65813100,65815040,65815050,65819300,65819400,65824991,65825497,65826612,65826720,65831000,65831020,65834000,65854500,65855080,65855110,65875500,65883045,65883048,65883051,65889700,65889800,65894900,65894991,65925000,65927000,65927001,65945200,65945400,65945500,65945600,65948000,65950200,65955000,65956000,65958000,65960000,65960001,65960001,65962000,65963071,65963600,65963700,65970000,65970001,65970320,65970700,65971010,65971050,65971500,65973501,65975002,65975300,65980500,65981500,65983000,65984000,65987000,65987000,65987001,65992500,65992500,65993000,65993001,65995000,65999020,65999200,65999410,65999463,66005100,66005400,66005600,66005800,66005900,66005950,66005960,66007000,66010000,66025000,66025500,66028000,66028500,66029000,66029010,66030000,66050500,66051000,66052080,66052081,66052500,66052600,66052800,66052900,66053200,66056000,66064000,66070004,66071375,66071380,66071382,66071384,66071385,66071390,66071392,66071395,66071397,66071450,66071470,66077500,66125000,66162000,66164600,66165000,66170100,66170500,66170600,66171400,66171500,66174000,66201100,66201200,66210000,66240060,66240080,66250001,66259650,66260001,66260050,66260110,66270000,66280000,66360000,66370000,66380100,66384000,66385000,66385500,66386000,66388000,66390090,66400050,66400325,66400355,66400360,66400380,66400390,66420160,66420250,66450001,66450010,66452500,66453000,66454800,66454900,66460000,66483600,66483800,66484000,66484500,66488000,66489000,66490000,66493000,66493900,66494000,66494500,66521000,66522000,66522100,66523000,66525100,66600000,66650000,66710000,66810000,66825000,66830000,66859000,66861000,66870000,66870000,66900000,66910000,66941000,66945000,66945000,66960008,66960008,67100000,70110000,70115000,70120000,70150000,70305000,70600000,70610000,70710000,70720000,70840080,70841500,70842000,70843000,70843500,70844200,70844300,70844500,70845000,71200000,71300000,71325000,71350001,71383000,71383300,71385500,71386000,71386500,71388000,71388600,71497000,71498000,71540000,71620400,71620450,71621000,71621500,71644000,71645000,71647000,71655000,71700000,71740000,71840000,71890500,71900000,71955000,72080000,72090000,72101000,72101100,72428000,72430050,72480000,72480001,72480100,72500000,72690000,72690080,72715000,72805000,72806000,72810000,72815000,72817000,72818000,72849000,72849000,72860000,72860080,72870900,72880000,73170000,73200040,73200060,73200080,73200500,73220000,73249000,73250000,73250500,73251000,73290000,73310000,73318000,73330200,73330250,73331000,73331800,73331850,73331900,73334500,73335000,73339000,73340000,73389000,73390000,73390100,73420040,73420080,73436000,73437000,73440000,73445000,73460000,73490000,73509000,73510000,73520000,73528000,73552000,73553000,73558000,73560000,73569000,73570000,73571000,73571500,73582000,73582500,73590000,73600200,73600300,73600390,73600400,73600550,73600600,73600700,73620000,73630000,73658000,73660000,73674500,73675000,73690001,73690002,73691000,73692100,73692200,73692500,73693500,73693700,73693800,73694000,73698500,73699000,73710000,73712000,73820000,73890000,73892000,73900000,73960000,74040080,74050000,74100000,74100000,74100000,74120700,74120800,74120900,74130000,74295000,74300000,74314970,74314980,74315000,74320000,74322000,74323000,74324000,74329000,74339000,74340000,74345000,74350000,74350100,74350900,74351000,74355000,74356000,74400000,74400080,74423080,74423100,74462000,74463000,74464500,74465000,74466000,74467000,74468000,74468500,74510000,74549990,74550000,74650000,74660000,74670000,74675000,74690001,74690100,74694000,74695000,74800000,74890000,75050000,75120000,75173000,75174000,75174500,75178000,75180000,75181000,75187000,75188000,75230000,75287000,75288000,75288100,75290000,75291000,75305000,75307000,75318000,75325000,75326000,75330000,75331000,75340000,75341000,75342000,75343000,75344000,75371000,75500000,75500000,80360200,80360300,80360400,80360600,81018900,81019000,82330000,82335000,82350000,82430000,82500000,82549000,83020000,83029900,83040000,83345000,83669000,85029000,85180000,85500010,85500100,86100600,86100800,86101000,86109000,86110000,86117000,86118000,86162000,86163000,86370000,86371000,86390900,86402000,86403000,86404000,86405000,86406000,86520000,86520100]
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







