from tkinter import *
import random
import re
import json
#pippo negro
#implementare il selezionabile
#implementare mostra/nascondi password

#prende il dict degli utenti dal file json
def FRead():
    f = open("users.json", "r")
    users = json.loads(f.read())
    f.close()
    return users

#sovrascrive il dict degli utenti del file json
def FWrite(users):
    f = open("users.json", "w")
    f.write(json.dumps(users))
    f.close()

#effettua il login con il tasto enter
def OnEnterLogin(event):
    GetData()

#prende lo user name con il tasto enter
def OnEnterNick(event):
    SkipNick()

#prende la password con il tast enter
def OnEnterPass(event):
    Skip1()

#prende i dati dalle entry ed effettua il login
def GetData():
    global nickName
    global lbLoggedIn
    nickName = entryCheckNick.get()
    checkPass = entryCheckPass.get()
    lbLoggedIn = Label(window, text = f"accesso eseguito come {nickName}", font = 12)

    users = FRead()
    
    #controlla se il nome inserito esiste
    if nickName in users:
        lbErrorNick2.place_forget()
        #controlla se la password inserita è corretta
        if checkPass == users[nickName]:
            lbErrorPass2.place_forget()
            LoggedIn()
        else:
            lbErrorPass2.place(x = 200, y = 230)
    else:
        lbErrorNick2.place(x = 200, y = 130)
   
#scegliere se impostare o generare la password 
def ChoicePass():
    lbErrorNick1.place_forget()
    lbTitleS.place_forget()
    lbInNick.place_forget()
    entryNick.place_forget()
    btNick.place_forget()
    
    lbChoice1.place(x = 200, y = 100)
    btChoice1.place(x = 200, y = 200)
    btChoice2.place(x = 400, y = 200)

#genera la password
def GeneratePass():
    password = ""
    for i in range(4):
        password += chr(random.randrange(55,91))
        password += chr(random.randrange(97,123))
    for i in range(4):
        password += chr(random.randrange(33,39))
    return password

#pagina di impostatura password
def Choice1():
    lbChoice1.place_forget()
    btChoice1.place_forget()
    btChoice2.place_forget()
    lbInPass.place(x = 245, y = 50)
    entryPass.place(x = 220, y = 90)
    btSkip1.place(x = 300, y = 160)
    
    #esegue la funzione del bottone se premuto l'enter
    entryPass.bind("<Return>", OnEnterPass)

#pagina di generazione password
def Choice2():    
    global entryNewPass
    
    users = FRead()
    users[nickName] = GeneratePass()
    FWrite(users)
    password = users[nickName]
    lbChoice1.place_forget()
    btChoice1.place_forget()
    btChoice2.place_forget()
    entryNewPass = Entry(window, state = "readonly", textvariable = password, relief = "flat")
    
    entryNewPass.place(x = 330, y = 105)
    lbNewPass.place(x = 250, y = 100)
    btSkip2.place(x = 300, y = 200)
    
#prende lo user name dalla entry e passa alla pagina di password
def SkipNick():
    global nickName
    nickName = entryNick.get()
    users = FRead()
    
    #pulisce il contenuto della entry
    entryNick.delete(0,END)
    
    #controlla se il nome inserito esiste già
    if nickName in users:
        lbErrorNick3.place(x = 250, y = 300)
    else:
        lbErrorNick3.place_forget()
        #controlla che il nome sia di almeno 5 caratteri
        if len(nickName) < 5:
            lbErrorNick1.place(x = 170, y = 300)
        else:
            FWrite(users)
            ChoicePass()

#prende la password dalla pagina di impostatura password e passa al login
def Skip1():
    regex = r"^(?=.*[A-Z])(?=.*\d.*\d)(?=.*[!@#$%^&*()_+~`|}{[\]:;'<>?,./])(?=.*[a-zA-Z]).{8,}$"
    
    users = FRead()
    users[nickName] = entryPass.get()
    FWrite(users)
    
    #pulisce il contenuto della entry
    entryPass.delete(0,END)
    
    #controlla se la password inserita soddisfa le condizioni
    if re.match(regex, users[nickName]):
        lbErrorPass1.place_forget()
        lbInPass.place_forget()
        entryPass.place_forget()
        btSkip1.place_forget()
        Login()
    else:
        lbErrorPass1.place(x = 200, y = 250)

#passa al login dopo la generazione della password 
def Skip2():
    lbNewPass.place_forget()
    entryNewPass.place_forget()
    btSkip2.place_forget()
    Login()

#pagina di registrazione    
def SignUp():
    lbErrorPass2.place_forget()
    lbErrorNick2.place_forget()
    lbChoice2.place_forget()
    btLogin1.place_forget()
    btSignUp.place_forget()
    entryCheckNick.place_forget()
    entryCheckPass.place_forget()
    lbUsr.place_forget()
    lbPass.place_forget()
    lbTitleL.place_forget()
    btLogin2.place_forget()
    lbTitleS.place(x = 310, y = 20)
    lbInNick.place(x = 250, y = 100)
    entryNick.place(x = 220, y = 150)
    btNick.place(x = 300, y = 200)
    
    #esegue la funzione del bottone se premuto l'enter
    entryNick.bind("<Return>", OnEnterNick)

#pagina di login    
def Login():
    lbChoice2.place_forget()
    btLogin1.place_forget()
    entryCheckNick.place(x = 180, y = 100)
    entryCheckPass.place(x = 180, y = 200)
    lbUsr.place(x = 50, y = 96)
    lbPass.place(x = 50, y = 196)
    lbTitleL.place(x = 270, y = 30)
    btLogin2.place(x = 500, y = 130)
    btSignUp.place(x = 500, y = 30)
    
    #esegue la funzione del bottone se premuto l'enter
    entryCheckPass.bind("<Return>", OnEnterLogin)

#pagina di logged in        
def LoggedIn():
    entryCheckNick.place_forget()
    entryCheckPass.place_forget()
    lbUsr.place_forget()
    lbPass.place_forget()
    lbTitleL.place_forget()
    btLogin2.place_forget()
    btSignUp.place_forget()
    lbLoggedIn.place(x = 170, y = 150)

window = Tk()
window.title("SaccoGay.org")
window.geometry("700x400+400+200")
window.resizable(0, 0)
nickName = ""

entryCheckNick = Entry(window, width = 40)
entryCheckPass = Entry(window, width = 40)
entryNick = Entry(window, width = 40)
entryPass = Entry(window, width = 40)

lbTitleL = Label(window, text = "Login", font = (60))
lbTitleS = Label(window, text = "Sign up", font = (60))
lbUsr = Label(window, text = "user name:", font = (12))
lbPass = Label(window, text = "nuova password:", font = (12))
lbNewPass = Label(window, text = "password:", font = (20))
lbInPass = Label(window, text = "inserire la nuova password:", font = 12)
lbErrorPass1 = Label(window, fg = "red", text = "\nla password deve essere composta da:\n-almeno 8 caratteri\n-2 numeri\n-1 lettera maiuscola\n-1 carattere speciale", font = (12))
lbErrorPass2 = Label(window, fg = "red", text = "password errata", font = (12))
lbChoice1 = Label(window, text = "impostare una password o generarne una?", font = (20))
lbChoice2 = Label(window, text = "registarsi o accedere?", font = (20))
lbInNick = Label(window, text = "inserire il nuovo nickname:", font = 12)
lbErrorNick1 = Label(window, fg = "red", text = "il nome utente deve essere di almeno 5 caratteri", font = 12)
lbErrorNick2 = Label(window, fg = "red", text = "il nome utente non esiste", font = 12)
lbErrorNick3 = Label(window, fg = "red", text = "il nome utente è già in uso", font = 12)

btLogin1 = Button(window, text = "login", command = lambda: Login(), height = 3, width = 10, bg = "grey")
btLogin2 = Button(window, text = "click", command = lambda: GetData(), height = 3, width = 10, bg = "grey")
btSignUp = Button(window, text = "sign up", command = lambda: SignUp(), height = 3, width = 10, bg = "grey")
btChoice1 = Button(window, text = "imposta", command = lambda: Choice1(), height = 3, width = 10, bg = "grey")
btChoice2 = Button(window, text = "genera", command = lambda: Choice2(), height = 3, width = 10, bg = "grey")
btSkip1 = Button(window, text = "avanti", command = lambda: Skip1(), height = 3, width = 10, bg = "grey")
btSkip2 = Button(window, text = "avanti", command = lambda: Skip2(), height = 3, width = 10, bg = "grey")
btNick = Button(window, text = "click", command = lambda: SkipNick(), height = 3, width = 10, bg = "grey")

#pagina di scelta se login o sign up
lbChoice2.place(x = 270, y = 100)
btLogin1.place(x = 200, y = 200)
btSignUp.place(x = 400, y = 200)

window.mainloop()