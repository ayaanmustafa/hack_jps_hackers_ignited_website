from tkinter import *
from tkinter.filedialog import askopenfilename 
import tkinter.font as font
import pyttsx3
import tensorflow as tf
from keras.preprocessing import image
from tensorflow import keras
from PIL import ImageTk,Image
model = keras.models.load_model('final_model.h5')
import numpy as np
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(text):
          print(text)
          engine.say(text)
          engine.runAndWait()

WIN = Tk()
WIN.geometry("350x350")
WIN.resizable(0,0)
WIN.configure(bg="blue2")
WIN.title("Flower classifier")
load = Image.open('Webp.net-resizeimage.jpg')
render = ImageTk.PhotoImage(load)
img = Label(WIN,image=render)
img.place(x=60,y=0)

WIN.iconbitmap('iconfinder_icon-80-document-file-ai_315878.ico')
Label(WIN,text="Art classifier",font=("Cambria bold",25),fg="Red",bg="#f8f8ff",pady=10).pack()
l = Label(WIN,text="",font=("Arial",10),fg='white',bg="green",pady=5)
myFont = font.Font(family='Helvetica', size=18, weight='bold')
l['font'] = myFont
l2 = Label(WIN,text="Confused about pencil sketch, pop art and water color painting?n Take help from this ML model",font=("Arial",18),fg='white',bg="red")

l2['font'] = myFont
def open():
	global WIN
	global l2
	myFont = font.Font(family='Helvetica', size=15, weight='bold')
	filename = askopenfilename(initialdir="/Pictures", filetypes =[('jpeg files', '*.jpg'),("all files","*.*")]) 	
	path = filename
	print(path)
	img = image.load_img(path, target_size=(200, 200))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	img = np.vstack([x])
	global download
	l2.destroy()
	global model
	classes = model.predict(img)

	global l
	l.place(x=45,y=120)
	for y in classes:
		if y[0] == 1:
			print("It's a pencil sketch")
			l['text'] = " It's a pencil sketch art  "
			speak(" It's a pencil sketch ")
		elif y[1] == 1:
			print(" It's a pop art painting  ")
			l['text'] = "  It's  pop art painting   "
			speak("It's  pop art painting")
		elif y[2] == 1:
			print("It's a watercolour painting")
			l['text'] = "It's a watercolour painting"
			speak("It's a watercolour painting") 
		else:
			print("I am not sure")
			l['text'] = "I am not sure"
			speak("I am not sure")
	download['text'] = "Open another image"
	download['font'] = myFont
	download.place(x=25,y=210)
	def exit():
		sys.exit()
	exit = Button(WIN,text="Exit",fg='white',bg="dark orange",command=exit)
	exit['font'] = myFont
	exit.place(x=280,y=210)



download = Button(WIN,text='  Open image ',font=("Arial bold",22),fg='white',bg="dark orange",command=open)
download.place(x=70,y=190) 



WIN.mainloop()
