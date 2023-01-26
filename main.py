import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser

openai.api_key=api_data

completion=openai.Completion()

def Reply(question):
    prompt=f'Juan: {question}\n Chatia: '
    response=completion.create(prompt=prompt, engine="text-curie-001", stop=['\Juan'], max_tokens=200)
    answer=response.choices[0].text.strip()
    return answer

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("rate",135)
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hola, en que puedo ayudarte? ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Escuchando...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Analizando.....")
        query=r.recognize_google(audio, language='es , en')
        print("Usuario dijo : {} \n".format(query))
    except Exception as e:
        print("Repitelo....")
        return "nada"
    return query


if __name__ == '__main__':
    while True:
        query=takeCommand().lower()
        ans=Reply(query)
        print(ans)
        speak(ans)
        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        if 'open google' in query:
            webbrowser.open("www.google.com")
        if 'bye' in query:
            break

