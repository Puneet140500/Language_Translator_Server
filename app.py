from flask import Flask, request, jsonify
from textblob import TextBlob
import json
from winsound import PlaySound
from googletrans import Translator , LANGUAGES
from flask_cors import CORS
import speech_recognition as sr

app = Flask(__name__)
CORS(app)

dic=('kannada','kn','telugu','te','hindi','hi','english','en')

@app.route("/api",methods=['GET','POST'])

def returnascii():
    if(request.method=='POST'):
        print("request worked")
        request_data = request.data
        request_data = json.loads(request_data.decode())
        
        text = request_data['text']
        lang = request_data['lang']
        s = Translate(text,lang)
        return s
    elif(request.method=='GET'):
        print("request worked")
        text = Record()
        src_lang = Translator().detect(text)
        print(src_lang)
        #lang = TextBlob(text)
        #src = lang.detect_language()
        return text



def Record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        r.adjust_for_ambient_noise(source) #reduce noise
        audio_text = r.listen(source)
        print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        return text
    except:
         return "Sorry, I did not get that"


def Translate(text,lang):
    translator = Translator()
    # stext = sys.argv[2]
    #stranslate=translator.translate(text= stext)
    translated=translator.translate(text= text ,  dest = lang)
    s = translated.text
    return s


if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')



