#!/usr/bin/python3

import sys, getopt, pyttsx3

# a simple script to speak out a book or write it into an mp3

# either read the book out aloud or save it to an mp3 file
def speak(bookfile, audiofile, voice, rate):
    engine = pyttsx3.init()
    if voice != '':
      engine.setProperty('voice', voice)      
    if rate != '':
      engine.setProperty('rate', int(rate))

   # clean up a bit on the text to remove newlines, but not remove paragraph lines
    book = open(bookfile, 'r').read()\
        .replace('\n\n', '*newline*')\
        .replace('\n', ' ')\
        .replace('*newline*', '\n\n')

    if audiofile == '':
       engine.say(book)
    else:
       engine.save_to_file(book, audiofile)
    
    engine.runAndWait()

# assumes running in a MacOS environment
def main(argv):
   book, audio, voice, rate = '', '', '', ''
   try:
      opts, args = getopt.getopt(argv,"hb:a:v:r",["book=","audio=","voice=","rate="])
   except getopt.GetoptError:
      print('speak.py -b <book-file> -a <audio-file> -v <voice-id> -r <words-per-min>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('speak.py -b <book-file> -a <audio-file> -v <voice-id> -r <words-per-min>')
         sys.exit()
      elif opt in ("-b", "--book"):
         book = arg
      elif opt in ("-a", "--audio"):
         audio = arg
      elif opt in ("-v", "--voice"):
         voice = arg
      elif opt in ("-r", "--rate"):
         rate = arg                  
   speak(book, audio, voice, rate)    

if __name__ == "__main__":
   main(sys.argv[1:])

