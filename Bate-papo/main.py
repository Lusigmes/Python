import flet as ft

def main(pagina):
    texto = ft.Text("Open Chat - CONVERSE AQUI!!!")
    chat = ft.Column()
    
    nome_user = ft.TextField(label= "Digite seu nome")
    
    def send_msg_(message):
        tipo = message["tipo"]
        if tipo == "message":
            text_message = message["text"]
            user_message = message["usuario"]
            #enviar msg no formato usuario: <texto>
            chat.controls.append(ft.Text(f"{user_message}: {text_message}"))
        else:
            user_message = message["usuario"]
            chat.controls.append(ft.Text(f"{user_message} entrou...",
                                         size=13,
                                         italic=True,
                                         color=ft.colors.AMBER_900))
            
        pagina.update()
        
    pagina.pubsub.subscribe(send_msg_)
    
    def send_message(event):
        #enviar msg no formato usuario: <texto>
        pagina.pubsub.send_all({"text": mensagens.value,
                                "usuario": nome_user.value,
                                "tipo":"message"})
        mensagens.value = ""
        pagina.update()

    mensagens = ft.TextField(label="digite aqui...", on_submit=send_message)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=send_message)
    
    def in_dialog(event):
        pagina.pubsub.send_all({"usuario": nome_user.value,
                                "tipo":"entrada"})
       
        pagina.add(chat)#bp
        dialog_.open = False #fecha o popup
        
        pagina.remove(botao_entrar)
        pagina.remove(texto)
            
            #input/submit
        row_mensage = ft.Row(
            [mensagens, botao_enviar]
        )
        pagina.add(row_mensage)
        pagina.update()
        
    dialog_ = ft.AlertDialog(open=False, 
                            modal=True, 
                            title=ft.Text("Entrar no bate papo"),
                            content=nome_user,
                            actions=[ft.ElevatedButton("Entrar", on_click=in_dialog)]
                            )
    
    def starter_chat(event):
        pagina.dialog = dialog_
        dialog_.open = True
        pagina.update()
        
    botao_entrar = ft.ElevatedButton("Comece agora !", on_click=starter_chat)
    
    pagina.add(texto)
    pagina.add(botao_entrar)
    
ft.app(target=main, view=ft.WEB_BROWSER, port=8090)
# ft.app(main)