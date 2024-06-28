import pyttsx3
import datetime
import speech_recognition as sr

texto_fala = pyttsx3.init()

rate = texto_fala.getProperty('rate')
texto_fala.setProperty('rate',190) # velocidade da fala
voices = texto_fala.getProperty('voices')
texto_fala.setProperty('voice',voices[0].id) # mudando a voz

def falar(audio):
    texto_fala.say(audio)
    texto_fala.runAndWait()
    
def tempo():
    hora = datetime.datetime.now().strftime('%H:%M') # caso queira os segundos %I:%M:%S
    falar(hora)
def data():
    Data = datetime.datetime.now().strftime('%d/%m/%Y')
    falar(Data)
    
    
def comprimento():
    hora = datetime.datetime.now().hour
    if 6 <= hora < 12:
        falar("Bom dia senhor Matarazzo!")
    elif 12 <= hora < 18:
        falar("Boa tarde senhor Matarazzo!")
    else:
        falar("Boa noite senhor Matarazzo!")
    falar("Como posso ajudar hoje?")

def microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Escutando...")
        audio = r.listen(source)
    try:
        print("Aguardando por seus comandos.")
        comando = r.recognize_google(audio,key=None,language='pt-br')
        print(comando)
    except sr.UnknownValueError:
        falar("Desculpe, não entendi o que você disse. Por favor, repita.")
        return None
    except sr.RequestError:
        falar("Desculpe, não consegui me conectar ao serviço de reconhecimento de voz.")
        return None

if __name__ == "__main__":
    comprimento()
    contador = 0
    
    while True:
        comando = microfone()
        if comando is None:
            continue
        if contador >= 3:
            falar("O sistema foi encerrado após três comandos. Muito obrigada e até a próxima.")
            break
        if "encerrar" in comando:
            falar("O sistema está sendo encerrado. Muito obrigada e até a próxima.")
            break
        if "hora" in comando:
            tempo()
        elif "data" in comando:
            data()
        elif "como você está" in comando:
            falar("Estou muito bem, obrigada por perguntar.")
            falar("O que posso fazer para ajudar hoje?")
        contador += 1
    
    
    
    

