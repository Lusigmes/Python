import speech_recognition as sr
import pyaudio

def ouvir_mic():
    mic = sr.Recognizer() #habilitar mic
    with sr.Microphone() as source: #redução de ruido
        mic.adjust_for_ambient_noise(source) #usuario pronto para ouvir
        print("Diga algo: ") #armazena audio na variavel
        audio = mic.listen(source)


    try: # tenta enviar o audio para o reconehcedor de padroes
        frase = mic.recognize_google_cloud(audio, language='pt-BR')
        print("O que foi dito: ", frase)
    except sr.UnknownValueError as e:
        print(f"ERRO: [{e}]")

    return frase

ouvir_mic()