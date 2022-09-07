from tkinter import *
import openai
import pyttsx3
import textwrap


root = Tk()
root.title("SmartBOT OpenAI")
root.geometry('800x700+400+100')
root.configure(bg='light grey')


BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
TEXT_COLOR2 = "#FF6242" 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

bubbles = []
engine2 = pyttsx3.init()
""" RATE"""
rate = engine2.getProperty('rate')  
engine2.setProperty('rate', 140)     


"""VOLUME"""
volume = engine2.getProperty('volume')   
engine2.setProperty('volume',1.0)   

"""VOICE"""
voices = engine2.getProperty('voices')      




def send():
    send = "Vous -> " + e.get() 
    txt.insert(END, "\n" + send)
    txt.insert(END, "\n" + "")
    root.after(500, receive)
    txt.see(END)
    
parole=[]

def receive():
    user = e.get().lower()    
    e.delete(0, END)
    openai.api_key = apikey.get()
    response = openai.Completion.create(
        engine=engine.get(),
        prompt=user,
        temperature=int(float(temperature.get())),
        max_tokens=int(maxtokens.get()),
        top_p=int(topp.get()),
        frequency_penalty=int(freqpen.get()),
        presence_penalty=int(prespen.get()),
        best_of=int(bestof.get()),
    )
    receivedmsg = "SmartBOT -> " + response["choices"][0]["text"]
    receivedmsg = receivedmsg.replace("\n", "")
    parole.append(receivedmsg)
    print(parole)
    receivedmsg = textwrap.fill(receivedmsg, 70)
    txt.insert(END, "\n" + receivedmsg)
    txt.insert(END, "\n" + "")
    txt.see(END)
    root.after(500, speak)





def clear_txt():
    txt.delete(1.0, END)

def clear_api():
    apikey.delete(0, END)

def speak():
    engine2 = pyttsx3.init()
    engine2.say(parole[-1].replace("SmartBOT -> ", ""))
    engine2.runAndWait()


def stop_talkin():
    engine2.stop()





#apikey field
apikey = Entry(root,width=26, font=("Helvetica", 10))
apikey.place(x=10, y=640, width=290, height=40)
#cache le texte avec des *
apikey.config(show="*")
apikey.insert(0,"Coller votre clé API OpenAI ici")
Label(root, text="API Key Field", font=("Helvetica", 10)).place(x=10, y=610, width=290, height=20)

#engine field
engine = Entry(root,width=26, font=("Helvetica", 10))
engine.place(x=670, y=35, width=125, height=20)
engine.insert(0,"text-davinci-002")
Label(root, text="Engine", font=("Helvetica", 10)).place(x=670, y=10, width=90, height=20)

#temperature field
temperature = Entry(root,width=26, font=("Helvetica", 10))
temperature.place(x=670, y=85, width=125, height=20)
temperature.insert(0,"0.7")
Label(root, text="Temperature", font=("Helvetica", 10)).place(x=670, y=60, width=90, height=20)

#max tokens field
maxtokens = Entry(root,width=26, font=("Helvetica", 10))
maxtokens.place(x=670, y=135, width=125, height=20)
maxtokens.insert(0,"256")
Label(root, text="Max Tokens", font=("Helvetica", 10)).place(x=670, y=110, width=90, height=20)

#top p field
topp = Entry(root,width=26, font=("Helvetica", 10))
topp.place(x=670, y=185, width=125, height=20)
topp.insert(0,"1")
Label(root, text="Top P", font=("Helvetica", 10)).place(x=670, y=160, width=90, height=20)

#frequency penalty field
freqpen = Entry(root,width=26, font=("Helvetica", 10))
freqpen.place(x=670, y=235, width=125, height=20)
freqpen.insert(0,"0")
Label(root, text="Frequ Penalty", font=("Helvetica", 10)).place(x=670, y=210, width=90, height=20)

#presence penalty field
prespen = Entry(root,width=26, font=("Helvetica", 10))
prespen.place(x=670, y=285, width=125, height=20)
prespen.insert(0,"0")
Label(root, text="Pres Penalty", font=("Helvetica", 10)).place(x=670, y=260, width=90, height=20)

#best of field
bestof = Entry(root,width=26, font=("Helvetica", 10))
bestof.place(x=670, y=335, width=125, height=20)
bestof.insert(0,"1")
Label(root, text="Best Of", font=("Helvetica", 10)).place(x=670, y=310, width=90, height=20)


#bouton clear txt
buton = Button(root, width=20, height=2,
relief='raised',state='active',command=clear_txt)
buton.config(text='Effacer conversation', bg='lightblue', font='Verdana 8 bold')
buton.place(x=310, y=610)

#bouton clear api
buton = Button(root, width=20, height=2,
relief='raised',state='active',command=clear_api)
buton.config(text='Effacer Clé API', bg='lightblue', font='Verdana 8 bold')
buton.place(x=310, y=650)

#bouton stop talking
buton = Button(root, width=20, height=2,
relief='raised',state='active',command=stop_talkin)
buton.config(text='Stop', bg='lightblue', font='Verdana 8 bold')
buton.place(x=670, y=610)



lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR2, text= "Bienvenue sur SmartBOT OpenAI", font=FONT_BOLD, pady=10, width=65, height=1).grid(
    row=0 , column=0, columnspan=2, padx=5, pady=2)

 
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2, padx=3, pady=1)
 
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
scrollbar.config(command=txt.yview)
txt.config(yscrollcommand=scrollbar.set)
txt.see(END)
 
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0 , padx=3, pady=1)
 
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)



root.mainloop()