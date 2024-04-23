#PEGAR POSIÇÃO ESPECIFICA PARA CADA "TIPO" DE TELA
#POIS A POSIÇÃO DO CLICK MUDA DE ACORDO COM A RESOLUÇÃO DA TELA

import pyautogui 
import time 

time.sleep(3)
print(pyautogui.position())

#usuario
# Point(x=670, y=373) # Point(x=570, y=371)
#senha
# Point(x=488, y=464)# Point(x=606, y=474)#Point(x=898, y=474)

#primeiro campo do form
# Point(x=756, y=254) # Point(x=583, y=256)


#          codigo       marca        tipo  categoria  preco_unitario  custo               obs
# 0    MOLO000251    Logitech       Mouse          1           25.95    6.5               NaN