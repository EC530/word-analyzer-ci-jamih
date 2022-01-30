import PyPDF2
import pdfplumber


def pdf_count_words():
    '''
    # creating a pdf file object
    pdfFileObj = open('poem.pdf', 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    print(pdfReader.numPages)

    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    print(pageObj.extractText())

    # closing the pdf file object
    pdfFileObj.close()
    '''

    pdf = pdfplumber.open('poem.pdf')
    page = pdf.pages[0]
    text = page.extract_text()
    print(text)
    print(type(text))
    pdf.close()


def main():
    pdf_count_words()
    
    
    
if __name__ == '__main__':
    main()
