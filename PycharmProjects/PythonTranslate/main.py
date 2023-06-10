from googletrans import Translator
from PyPDF2 import PdfReader

translator = Translator()

PageNumber = input("Which Page Do You Want To Translate:")

reader = PdfReader("YourPdfPath")
page = reader.pages[int(PageNumber)-1]
inputtext = page.extract_text()


OutputLang = input("Which Language Do you Want : ")

translations = translator.translate(inputtext, dest=OutputLang)

print(translations.text)

outputfile = input("Enter a name for output file: ")

dosya = open(f"{outputfile}.txt", "w")
dosya.write(translations.text)
