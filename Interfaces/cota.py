import requests #pip install requests
from tkinter import *

def get_cotacao():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    req_ = request.json()
    
    cota_dol = req_['USDBRL']['bid']
    cota_eur = req_['EURBRL']['bid']
    cota_btc = req_['BTCBRL']['bid']
    
    txt = f'''
    ********************
    Dólar: {cota_dol}
    
    Euro: {cota_eur}
    
    Bitcoin: {cota_btc}
    ********************
    '''
    txt_result["text"] = txt
    btn_fechar["state"] = NORMAL  # Habilita o botão de fechar

def fechar_info():
    txt_result["text"] = ""
    btn_fechar["state"] = DISABLED 
    
# janela
window = Tk()

window.title("Cotação de Moedas")
window.geometry("300x400")

txt_inicial = Label(window,text="Exibir cotação atual do Dólar | Euro | BTC")
txt_inicial.grid(column=0,row=0, padx=40, pady=50)

btn_ver = Button(window, text="Ver Cotações", command=get_cotacao)
btn_ver.grid(column=0,row=1, padx=10, pady=10)

btn_fechar = Button(window,  text="Fechar", command=fechar_info, state=DISABLED)
btn_fechar.grid(column=0,row=2,padx=10,pady=10)

txt_result = Label(window, text="")
txt_result.grid(column=0,row=3, padx=10, pady=50)

window.mainloop()