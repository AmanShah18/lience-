import requests
import json 
import time
from win32com.client import Dispatch

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=d562a3b63db540519249259e51be58e2")
Q=data.text
s=json.loads(Q)
# print(s)
print(type(s["articles"]))
for dict in s["articles"]:
    t= dict["title"]
    c=dict["content"]
    final=f"the title is{t} and the main news is {c}"
    print(f"the title is{t} \n and the main news is {c} \n")
    speak(final)
