#!/usr/bin/python3
import pdfplumber
import sys
from gtts import gTTS

language = 'en'
# book = sys.argv[1]


def read_book(book):
    with open(book, 'r', encoding=ISO8859-1) as f:
        text = f.read()
    return text


def speak(text):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save('book.mp3')
    # os.system('mpg321 book.mp3')


if __name__ == '__main__':
    book = sys.argv[1]
    text = read_book(book)
    speak(text)
