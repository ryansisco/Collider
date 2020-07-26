#!/usr/bin/env python


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from shutil import copyfile
from filehash import FileHash
import time
import subprocess

primaryfile=""
secondaryfile=""

window = Tk()
window.title("Collider")
window.geometry("500x250")


def hashit(typeh, sizey, primary, secondary):
	extp = ""
	exts = ""
	if len(primary) > 0 and len(secondary) > 0:
		if primary.split(".")[-1] != primary:
			extp = primary.split(".")[-1]
		if secondary.split(".")[-1] != secondary:
			exts = secondary.split(".")[-1]
		try:
			copyfile(primary, "./primary." + extp)
			copyfile(secondary, "./secondary." + exts)
		except IOError as er:
			print("Fail copying files: %s" % e)
			exit()

		if typeh == "MD5":
			hasher = FileHash('md5')
		if typeh == "SHA1":
			hasher = FileHash('sha1')
		if typeh == "SHA256":
			hasher = FileHash('sha256')

		primaryHash = hasher.hash_file("./primary." + extp)
		pHash.set(primaryHash)
		while True:
			secondaryHash = hasher.hash_file("./secondary." + exts)
			sHash.set(secondaryHash)
			if secondaryHash[:sizey] != primaryHash[:sizey]:
				with open("./secondary." + exts, "ab") as bwrite:
					by = bytes("0", 'utf-8')
					bwrite.write(by)
				bwrite.closed
			else:
				break
			window.update_idletasks()

		stbut.configure(text="Start")
		
def choosePrim():
	global primaryfile
	primaryfile = filedialog.askopenfilename(title="First File")
	primary.configure(text=primaryfile)
		

def chooseSec():
	global secondfile
	secondfile = filedialog.askopenfilename(title="Second File")
	secondary.configure(text=secondfile)

def runny():
	stbut.configure(text="Hashing...")
	window.update_idletasks()
	prim = primary["text"]
	seco = secondary["text"]
	if hashtype.get() == 1:
		hashit("MD5", md5.get(), prim, seco)
	if hashtype.get() == 2:
		hashit("SHA1", sha1.get(), prim, seco)
	if hashtype.get() == 3:
		hashit("SHA256", sha2.get(), prim, seco)
	stbut.configure(text="Start")
	window.update_idletasks()


seconly = IntVar()
hashtype = IntVar()
md5 = IntVar()
sha1 = IntVar()
sha2 = IntVar()
pHash = StringVar()
sHash = StringVar()


Button(window, text="Primary File: ", command=choosePrim, width=30).grid(column=0, row=0, sticky=W)
Button(window, text="Secondary File: ", command=chooseSec, width=30).grid(column=0, row=1, sticky=W)
primary = Label(window, fg="Red", justify=LEFT, anchor="w", width=50)
secondary = Label(window, fg="Blue",justify=LEFT, anchor="w", width=50)
primary.grid(column=1, row=0, sticky=W)
secondary.grid(column=1, row=1, sticky=W)


Radiobutton(window, text="MD5", variable=hashtype, value=1, width=15).grid(column=0, row=3, sticky=W)
Radiobutton(window, text="SHA1", variable=hashtype, value=2, width=15).grid(column=0, row=4, sticky=W)
Radiobutton(window, text="SHA256", variable=hashtype, value=3, width=15).grid(column=0, row=5, sticky=W)

Scale(window, from_=1, to=32, variable=md5, orient=HORIZONTAL).grid(column=1, row=3, sticky=W)
Scale(window, from_=1, to=40, variable=sha1, orient=HORIZONTAL).grid(column=1, row=4, sticky=W)
Scale(window, from_=1, to=64, variable=sha2, orient=HORIZONTAL).grid(column=1, row=5, sticky=W)

Label(window, fg="Red", width=50)

stbut = Button(window, text="Start", command=runny, width=60, activebackground="grey")
stbut.grid(column=0, row=6, sticky=W, columnspan=2)

Label(window, text="Primary Hash:").grid(column=0, row=7, sticky=W)
Label(window, text="Secondary Hash:").grid(column=0, row=8, sticky=W)
Label(window, fg="Red", textvariable=pHash, justify=LEFT, anchor="w").grid(column=1, row=7, sticky=W)
Label(window, fg="Blue", textvariable=sHash, justify=LEFT, anchor="w").grid(column=1, row=8, sticky=W)

window.mainloop()