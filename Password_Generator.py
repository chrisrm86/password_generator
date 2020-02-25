#!/usr/bin/python3
# -*- coding UTF-8 -*-
"""
##########################################################

Name: 		Password generator
Created by: Christian Morán
e-mail: 	christianrmoran86@gmail.com
More code: 	http://github.com/chrisrm86

##########################################################
"""
from tkinter import *
from tkinter.messagebox import *
import random
import string
from sys import exit


class Password_generator:

	def __init__(self, parent=None, **config):
		self.frame = parent
		self.frame.geometry("300x90")
		self.frame.resizable(False, False)
		self.frame.title("Password Generator")

		self.container = Frame(self.frame, bg="white")
		self.container.pack(expand=YES, fill=BOTH)

		self.container_spaceTop = Frame(self.container, bg="white", height=10)
		self.container_spaceTop.pack(side=TOP, expand=NO, fill=BOTH)
		self.container_text = Frame(self.container, height=10,bg="white")
		self.container_text.pack(expand=NO, fill=BOTH)
		self.container_middle = Frame(self.container, bg="white", height=10)
		self.container_middle.pack(side=TOP, expand=NO, fill=BOTH)
		self.container_button = Frame(self.container, height=10,bg="white")
		self.container_button.pack(expand=NO, fill=BOTH)

		label_password = Label(self.container_text, text="PASSWORD: ", width=10, bg="white", fg="blue").pack(side=LEFT ,padx=10)

		visor = Label(self.container_text, text="", width=100, bg="LightGray")
		visor.pack(side=RIGHT, padx=10)

		def generate(stringLength=12):
			lettersAndDigits = string.ascii_letters + string.digits
			result = str(''.join(random.choice(lettersAndDigits) for i in range(stringLength)))
			visor.config(text=result)

		btn_generate = Button(self.container_button, text="Generate", command=generate).pack()

		def copy():
			r = visor
			copy = r.cget("text")
			r.clipboard_clear()
			r.clipboard_append(copy)
			r.update()

		def messageCreatedFile():
			showinfo(title="Message", message="A file with name 'Password' has been created in the directory where this program exist and contains your password.")

		def createFile():
			r = visor
			copy = r.cget("text")
			newFile = "Password"
			nf = open(newFile, 'w+')
			nf.write("This is the code: " + copy + '\r' + '\r' + "Thanks for use Password Generator." + '\r' + "Important! Don't forget delete this file.")
			nf.close()
			messageCreatedFile()

		def info():
			showinfo(title='Info',
				message="""Press 'Generate' button and then press 'Copy'. \rYour password is now on the clipboard.\rIf you want to create a file that contain your generated password you must be press 'Save to file'.""")

		def about():
			showinfo(title="About", message="""Developed by Christian Moran. Email:christianrmoran86@gmail.com.'\rMore code: www.github.com/chrisrm86 """)

		menubar = Menu(self.frame)
		menubar.add_command(label="Generate", command=generate)
		menubar.add_command(label="Copy", command=copy)
		menubar.add_command(label="Save to file", command=createFile)

		menuAbout = Menu(menubar, tearoff=0)
		menuAbout.add_command(label="How to use", command=info)
		menuAbout.add_command(label="About", command=about)
		menubar.add_cascade(label="Help", menu=menuAbout)
		menubar.add_command(label="Exit", command=exit)

		self.frame.config(menu=menubar)
		
if __name__ == '__main__':
	root = Tk()
	Password_generator(root)
	root.mainloop()