# pip install SpeechRecognition

# Linux:
# sudo apt-get install python-pyaudio python3-pyaudio
# MacOS:
# brew install portaudio
# pip install pyaudio
# Windows:
# pip install pyaudio

import speech_recognition as sr

print("Speech Recognition Version: "+sr.__version__)
r = sr.Recognizer()
# Micrófono por defecto
mic = sr.Microphone()
# Lista de micrófonos
#sr.Microphone.list_microphone_names()
#mic = sr.Microphone(device_index=7)

matches = ["PRENDER", "ENCENDER", "SWITCH ON"]

with mic as source:
    print("Grabando...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print("Traduciendo...")
    try:
        text = r.recognize_google(audio)
        text = text.upper()
        print(text)
        if any(x in text for x in matches): #any or all
            print("Prendiendo")
    except sr.UnknownValueError:
        print("Google Cloud Speech no pudo entener el audio")
    except sr.RequestError as e:
        print("No es posible consultar el servicio de Google Cloud Speech; {0}".format(e))