import pandas as pd
import pdf
import CalculoDeHoras as ch

disctHours = pdf.extrairPdf('relatorio.pdf')

listDates = disctHours.keys()
listHours = disctHours.values()
listHoursWorker = ch.calculaHorasDict(disctHours).values()
listaMinutosProporcionais = ch.calculaMinutosProporcionais(listHoursWorker)
listaConvertida = ch.converteDTToStr(listHoursWorker)

dictWorker = {'Data': listDates,
              'Pontos Batidos': listHours,
              'Horas Trabalhadas': listaConvertida,
              'Proporcional em minutos': listaMinutosProporcionais}



dictWorker = pd.DataFrame(dictWorker).to_string()


arquivo = open('HorasTrabalhadas.txt', 'w') 

arquivo.write(dictWorker)