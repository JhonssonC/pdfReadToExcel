#https://www.delftstack.com/es/howto/python/read-pdf-in-python/#:~:text=Utilice%20el%20m%C3%B3dulo%20PyPDF2%20para%20leer%20un%20PDF%20en%20Python,-PyPDF2%20es%20un&text=Abrimos%20el%20documento%20PDF%20en,PDF%20para%20leer%20el%20documento.
import pdfplumber
#https://www.geeksforgeeks.org/python-create-and-write-on-excel-file-using-xlsxwriter-module/#:~:text=XlsxWriter%20is%20a%20Python%20module,conditional%20formatting%20and%20many%20others.
import xlsxwriter
def leerPdf():
    with pdfplumber.open("Samanes2.pdf") as temp:
        print(len(temp.pages))
        workbook = xlsxwriter.Workbook('samanes2.xlsx')
        worksheet = workbook.add_worksheet()
        for page in temp.pages:
            data = page.extract_text()
            separador = "\n"
            data = data.split(separador)

            print(f'Pagina: {temp.pages.index(page) + 1}')

            for i in range(21):

                worksheet.write(temp.pages.index(page)+1, i, data[i])



    workbook.close()

        #first_page = temp.pages[0]
        #print(first_page.extract_text())


if __name__ == '__main__':
    leerPdf()

