from words import words
from tkinter import *

Mainscreen= Tk()
Mainscreen.geometry('800x600')
Mainscreen.title('Typing Test')
Mainscreen.config(bg="orange")

startlabel=Label(Mainscreen,text='Start Typing',font=('arial',30,
                  'italic bold'),bg='black',fg='white')
startlabel.place(x=275,y=50)

labelforward=Label(Mainscreen,text=words[0],font=('arial',45,
                'italic bold'),fg='green')
labelforward.place(x=250,y=240)

gameinstruction= Label(Mainscreen,text='Hit enter button after typing the word',
                       font=('arial',25,'italic bold'),fg='grey')
gameinstruction.place(x=150,y=500)

wordentry= Entry(Mainscreen,font=('arial',25,'italic bold'),bd=10,justify='center')
wordentry.place(x=250,y=330)
wordentry.focus_set()

Mainscreen.bind('<Return>',game)
mainloop()
