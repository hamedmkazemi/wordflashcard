# This code was done by hamedmkazemi
from PyDictionary import PyDictionary
from win10toast import ToastNotifier
import time
import requests
import random
import pyttsx3

r=requests
x=r.get('https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co')
x=x.text.split('\n')

dictionary=PyDictionary()
toaster = ToastNotifier()
engine = pyttsx3.init()
engine.setProperty('rate', 125)

wordlist=[]
for t in range(100):
    wordlist.append(random.choice(x))

def dict(i):
    text=''
    for k in dictionary.meaning(i).keys():
        text=k[:1].lower()+ ': '+dictionary.meaning(i)[k][0]+ "\n" +text
    return text.replace('(','')

while True:
    for i in wordlist:
        try:
            # windows notification
            meaning=dict(i)
            toaster.show_toast(i, meaning, duration=9*60, threaded=True)
            print(wordlist.index(i) + 1, '-', i,'\n'
                  'means:')
            print(meaning)
            print('*****************************************************')
            time.sleep(0.04 * 60)
            # text to speech
            engine.say(i)
            engine.runAndWait()
            time.sleep(10*60)
        except:
            pass