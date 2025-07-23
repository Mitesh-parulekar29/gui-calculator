import tkinter as tk
import math

f=("Segoe UI",30,"bold")
def butt_clic(num):
    tmp=screen.get()
    screen.delete(0,tk.END)
    screen.insert(0,tmp + str(num))

def butt_sqr():
	try:
		val=float(screen.get())
		res=val**2
		screen.delete(0,tk.END)
		screen.insert(0,str(res))
	except:
		screen.delete(0,tk.END)
		screen.insert(0,"ERROR..!")

def butt_sqrt():
	try:
		val=float(screen.get())
		res=math.sqrt(val)
		screen.delete(0,tk.END)
		screen.insert(0,str(res))
	except:
		screen.delete(0,tk.END)
		screen.insert(0,"ERROR..!!")


def butt_ac():
    screen.delete(0,tk.END)
        
def butt_ans():
    try:
        res=eval(screen.get().replace("x", "*"))
        screen.delete(0,tk.END)
        screen.insert(0,str(res))
    except:
        screen.delete(0,tk.END)
        screen.insert(tk.END,"ERROR..!")

calci=tk.Tk()
calci.title("Calculator")
calci.geometry("500x650")
calci.resizable(False, False)
calci.configure(bg="#A9A9A9")
calci.grid_rowconfigure(5,weight=1)

screen=tk.Entry(calci,font=("Segoe UI", 30,"bold"), bd=12, relief="sunken", justify="right")
screen.grid(row=0, column=0, columnspan=4, padx=30, pady=30,ipadx=40, ipady=30)

butt_sqr=tk.Button(calci, text="x²",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=butt_sqr)
butt_sqrt=tk.Button(calci, text="√",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=butt_sqrt)
butt_percent=tk.Button(calci, text="%",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic("%"))
butt_00=tk.Button(calci, text="00",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic("00"))

butt1=tk.Button(calci, text="1",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic(1))
butt2=tk.Button(calci, text="2",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic(2))
butt3=tk.Button(calci, text="3",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic(3))
butt4=tk.Button(calci, text="4",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic(4))
butt5=tk.Button(calci, text="5",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic(5))
butt6=tk.Button(calci, text="6",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic(6))
butt7=tk.Button(calci, text="7",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic(7))
butt8=tk.Button(calci, text="8",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic(8))
butt9=tk.Button(calci, text="9",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic(9))
butt0=tk.Button(calci, text="0",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic(0))


butt_add=tk.Button(calci, text="+",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic("+"))
butt_sub=tk.Button(calci, text="-",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic("-"))
butt_mul=tk.Button(calci, text="x",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic("x"))
butt_div=tk.Button(calci, text="/",font=f, padx=30,pady=30,relief="raised", highlightbackground="#87CEEB", highlightthickness=2,command=lambda:butt_clic("/"))

butt_ac=tk.Button(calci, text="C",font=f, padx=30,pady=30,relief="raised",bg="#f44336",fg="white", highlightbackground="#87CEEB", highlightthickness=2,command=butt_ac)
butt_ans=tk.Button(calci, text="=",font=f, padx=30,pady=30,relief="raised", bg="#4CAF50",fg="white",highlightbackground="#87CEEB", highlightthickness=5,command=butt_ans)

butt_sqr.grid(row=1,column=0,padx=8, pady=8,sticky="nsew")
butt_sqrt.grid(row=1,column=1,padx=8, pady=8,sticky="nsew")
butt_percent.grid(row=1,column=2,padx=8, pady=8,sticky="nsew")
butt_00.grid(row=1,column=3,padx=8, pady=8,sticky="nsew")

butt1.grid(row=2,column=0,padx=8, pady=8,sticky="nsew")
butt2.grid(row=2,column=1,padx=8, pady=8,sticky="nsew")
butt3.grid(row=2,column=2,padx=8, pady=8,sticky="nsew")
butt4.grid(row=2,column=3,padx=8, pady=8,sticky="nsew")

butt5.grid(row=3,column=0,padx=8, pady=8,sticky="nsew")
butt6.grid(row=3,column=1,padx=8, pady=8,sticky="nsew")
butt7.grid(row=3,column=2,padx=8, pady=8,sticky="nsew")
butt8.grid(row=3,column=3,padx=8, pady=8,sticky="nsew")

butt9.grid(row=4,column=0,padx=8, pady=8,sticky="nsew")
butt0.grid(row=4,column=1,padx=8, pady=8,sticky="nsew")
butt_ac.grid(row=4,column=2,padx=8, pady=8,sticky="nsew")
butt_ans.grid(row=4,column=3,padx=8, pady=8,rowspan=2,sticky="nsew")

butt_add.grid(row=5,column=2,padx=8, pady=8,sticky="nsew")
butt_sub.grid(row=5,column=1,padx=8, pady=8,sticky="nsew")
butt_mul.grid(row=5,column=0,padx=8, pady=8,sticky="nsew")
butt_div.grid(row=5,column=3,padx=8, pady=8,sticky="nsew")

for i in range(5):
    calci.grid_rowconfigure(i, weight=1)
    calci.grid_columnconfigure(i, weight=1)

calci.mainloop()
