from PyPDF2 import PdfReader
import CalculoDeHoras as ch

def extrairPdf(entrada):

    reader = PdfReader(entrada)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    listHours = text.split('\n')

    listHours = listHours[44:]

    
    listHours = [i for i in listHours if i != '']
    discHours = ch.convertListToDict(listHours)
    # discHours = {i: k for i, k in  discHours.items()}
    
    disc_hour = {i: k for i , k in discHours.items() if k != "Feriado" if k != "Folga" if k != "DSR" if k != "Compensação Dia" if k != "Férias"}

    return disc_hour

