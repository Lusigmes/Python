import pyautogui 
import time 
import pandas

pyautogui.PAUSE = 1
#abrir navegador
pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("enter")

#entar no site
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
pyautogui.press("enter")

#clica e preenche os campos de usuario e senha para fazer login
time.sleep(2)
pyautogui.click(x=670, y=373) #pos usuario
pyautogui.write("pythonimpressionador@gmail.com")
time.sleep(1)
pyautogui.press("tab") # pyautogui.click(x=898, y=474) #pos senha
pyautogui.write("sua senha")
pyautogui.press("enter")

#importar o csv
tabela_produtos = pandas.read_csv("produtos.csv")
print(tabela_produtos)

#cadastrar produtos
for linhaTabela in tabela_produtos.index:
    pyautogui.click(x=756, y=254)  #clicar no primeiro input do form  # pyautogui.press("tab") #entrar no primeiro input do form
#escrever codigo
    codigo = tabela_produtos.loc[linhaTabela,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab") 
#escrever marca
    marca = tabela_produtos.loc[linhaTabela,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab") 
#escrever tipo
    tipo = tabela_produtos.loc[linhaTabela,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab") 
#escrever categoria
    categoria = tabela_produtos.loc[linhaTabela,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab") 
#escrever preço unitario
    preco = tabela_produtos.loc[linhaTabela,"preco_unitario"]
    pyautogui.write(str(preco)) 
    pyautogui.press("tab") 
#escrever custo total
    custo = tabela_produtos.loc[linhaTabela,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab") 
#escrever obs
    obs = tabela_produtos.loc[linhaTabela,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab") 
#finalizar   
    pyautogui.press("enter") 

    pyautogui.scroll(2000)   # pyautogui.click(x=756, y=254)  #clicar no primeiro input do form





#---------------------------------------------------------observações-----------------------------------------------------------#
#exemplos fornecidos pela hashtag programação
#https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pythonimpressionador@gmail.com
#sua senha

#rpa 
# pyautogui.click # pyautogui.write # pyautogui.press #pyautogui.hotkey #pyaytogui.scroll() *negativo=baixo positivo=cima*
# pyautogui.press("enter\"") pressionar/ler com barra