from datetime import timedelta
import re

def entradadeDados(entrada1):
    entrada1 = entrada1.strip().split(" ")
    horarios1 = []

    for horario1 in entrada1:
        horario2 = horario1.split(':')
        horarios1.append(timedelta(hours=int(horario2[0]), minutes=int(horario2[1])))
    return horarios1

def CalculaHoraDeSair(horarios1, totalHorasTrabalhadas):   
    horaSair = totalHorasTrabalhadas[0] - (horarios1[1] - horarios1[0])
    horaSair += horarios1[2]
    return horaSair

def calculoDeHorasDia(horarios1):     
    totalTrabalhados = horarios1[1] - horarios1[0]
    totalTrabalhados += horarios1[3] - horarios1[2]
    if len(horarios1) > 5:
        totalTrabalhados += horarios1[5] - horarios1[4]    
    return totalTrabalhados

def convertListToDict(listas):
    padrao_horarios = r'^\d{2}:\d{2}(\s\d{2}:\d{2})*$'
    padrao_data = r"\b\d{1,2}/\d{1,2}\b"
    lista_dia_horas = []

    for valor in listas:
        if re.match(padrao_horarios, valor.strip()) or re.match(padrao_data, valor.strip()):
            lista_dia_horas.append(valor.strip())
        elif "Feriado" in valor:
            lista_dia_horas.append(valor.strip())
        elif "Folga" in valor:
            lista_dia_horas.append(valor.strip())
        elif "DSR" in valor:
            lista_dia_horas.append(valor.strip())
        elif "Compensação Dia" in valor:
            lista_dia_horas.append(valor.strip())
        elif "Férias" in valor:
            lista_dia_horas.append(valor.strip())

    lista_dia_horas = {lista_dia_horas[i]: lista_dia_horas[i+1] for i in range(0, len(lista_dia_horas), 2)}
    return lista_dia_horas     


def calculaHorasDict(discHours):
    discHours2 = {i: calculoDeHorasDia(entradadeDados(k)) for i , k in discHours.items() 
                  if k != "Feriado" if k != "Folga" if k != "DSR" if k != "Compensação Dia" if k != "Férias"}
    return discHours2

def converteDTToStr(entrada):
    listStrings = []
    for i in entrada:     
        i = str(i).split(":")
        hora = i[0]
        minuto = i[1]
        segundo = i[2]
        horaCompleta = hora + ":" + minuto + ":" + segundo
        listStrings.append(horaCompleta)
    return listStrings

def calculaMinutosProporcionais(lista):
    listaComProporcionais = []
    for i in lista:        
        x = str(i).split(':')
        hora = x[0]
        minuto = str(round(int(x[1])/ 60 * 100))
        if len(minuto) == 1:
            minuto = minuto + '0' 
        horaCompleta = hora + ":" + minuto
        listaComProporcionais.append(horaCompleta)
    return listaComProporcionais
