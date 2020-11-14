import os, sys, getopt, pytesseract, pdf2image, PIL

# extract text from PDF using OCR
def extract(pdf, text, first, last):
    f = int(first) if first else None
    l = int(last) if last else None

    print("Converting PDF to images ...")
    pages = pdf2image.convert_from_path(pdf, dpi=500, first_page=f, last_page=l) 
    print("Number of pages converted:", len(pages))
    f = open(text, "a") 
    print("Reading images and OCR to text ...")
    counter = 1
    for page in pages:
        pg = str(((pytesseract.image_to_string(page)))) 
        print("Page", counter, "of", len(pages))
        pg = pg.replace('-\n', '')
        f.write(pg)
        counter += 1
    f.close()

def main(argv):
   pdf, text, first, last = '', '', '', ''
   try:
      opts, args = getopt.getopt(argv,"hp:t:f:l:",["pdf=","text=","first=","last="])      
   except getopt.GetoptError:
      print('extract.py -p <pdf-file> -t <text-file> -f <first-page> -l <last-page>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('extract.py -p <pdf-file> -t <text-file> -f <first-page> -l <last-page>')
         sys.exit()
      elif opt in ("-p", "--pdf"):
         pdf = arg
      elif opt in ("-t", "--text"):
         text = arg
      elif opt in ("-f", "--first"):
         first = arg
      elif opt in ("-l", "--last"):
         last = arg
        
   extract(pdf, text, first, last)

if __name__ == "__main__":
   main(sys.argv[1:])