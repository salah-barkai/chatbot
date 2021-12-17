import tkinter as tk 
from tkinter import *



def send():
    send = "Vous-> "+Message.get()
    txt.insert(END, " "+send)
    user = Message.get().lower()
    if(user == "Salut"or user=="bonjour"or user=="hi"):
        txt.insert(END,  "" + "Bot -> salut")
    elif(user == "vous allez bien" or user == "comment cava" or user == "tout va bien"):
        txt.insert(END, " " + "Bot -> merci se super")
    elif(Message.get() == "Quoi de special"):
        txt.insert(END, " " + "Bot -> Rien de specail et toi?")
    elif(user == "Rien" or user == "super" or user == "Bien"):
        txt.insert(END, " " + "Bot -> super bien que fais tu ?")
    else:
        txt.insert(END, " " + "Bot -> Desolé je ne comprends pas ")
    Message.delete(0, END)







root = Tk()
root.title("Chat Bot")
root.config(bg="darkblue")


titre=Label(text="Message")
titre.pack(pady=40)
titre.config()


txt = Text()
txt.pack()

Message=Entry(width=100)
Message.pack(pady=15)

send = Button(root, text="Send",command=send)
send.pack(pady=5)




root.mainloop()