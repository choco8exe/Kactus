from dhooks import Webhook
from pystyle import *
from os import system
import time

name = """

   ▄█   ▄█▄    ▄████████  ▄████████     ███     ███    █▄     ▄████████ 
  ███ ▄███▀   ███    ███ ███    ███ ▀█████████▄ ███    ███   ███    ███ 
  ███▐██▀     ███    ███ ███    █▀     ▀███▀▀██ ███    ███   ███    █▀  
 ▄█████▀      ███    ███ ███            ███   ▀ ███    ███   ███        
▀▀█████▄    ▀███████████ ███            ███     ███    ███ ▀███████████ 
  ███▐██▄     ███    ███ ███    █▄      ███     ███    ███          ███ 
  ███ ▀███▄   ███    ███ ███    ███     ███     ███    ███    ▄█    ███ 
  ███   ▀█▀   ███    █▀  ████████▀     ▄████▀   ████████▀   ▄████████▀  
  ▀                                                                   

  """


Anime.Fade(Center.Center(name), Colors.yellow_to_red, Colorate.Vertical, interval=0.025, enter=True)

print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(name)))

webhook_url = Write.Input("url du webhook -> ", Colors.yellow_to_red, interval=0.008)
msg = Write.Input("quelle est votre message a envoyer -> ", Colors.yellow_to_red, interval=0.008)



while True:
    hook = Webhook(webhook_url)
    hook.send(msg)
    print("message envoyer avec succes !!")

   

    

#https://discord.com/api/webhooks/901520993925890068/6V6kdNIzJQ4sBbYHtlCLqdO3xYB_-1B9SryJ3youwCABVqVdzrvQdmbiiT6GLSm2P9YD