import functools
import os
import tkinter as tk
from concurrent import futures
from tkinter import ttk
from tkinter import *
import csv
import time
import datetime

thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)
 
 
def tk_after(target):
 
    @functools.wraps(target)
    def wrapper(self, *args, **kwargs):
        args = (self,) + args
        self.after(0, target, *args, **kwargs)
      
 
    return wrapper

def submit_to_pool_executor(executor):
 
    def decorator(target):
 
        @functools.wraps(target)
        def wrapper(*args, **kwargs):
            return executor.submit(target, *args, **kwargs)
 
        return wrapper
 
    return decorator

class MainFrame(tk.Frame):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        self.master.geometry('300x300')
        self.master.title("IPmtr")
        self.entry = tk.StringVar()
        self.entry2 = tk.StringVar()
        self.total = DoubleVar(value=0.0)
        self.total2 = DoubleVar(value=0.0)

        
        
        label = tk.Label(
            self.master, text="AP1.")
        label.pack()
        entry = tk.Entry(self.master, textvariable=self.entry)
        entry.insert(-1, "8.8.8.8")
        entry.pack()


        self.etiq6 = ttk.Label(self.master, textvariable=self.total,
                               foreground="yellow", background="black",
                               borderwidth=5, anchor="e")                                
        self.separ1 = ttk.Separator(self.master, orient=HORIZONTAL)

        self.etiq6.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=20, pady=5)        
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        
        resultt = os.system("ping -n 1 -w 500 " +self.entry.get()+ " > nul")
  
        if resultt == 0:
           self.total.set("¡OK!")  
        else:
           self.total.set("¡ERROR11!")
           os.system("communicator1.mp3")

       
        
        label = tk.Label(
            self.master, text="AP12.")
        label.pack()
        entry = tk.Entry(self.master, textvariable=self.entry2)
        entry.insert(-1, "1.1.1.1")
        entry.pack()

        self.etiq7 = ttk.Label(self.master, textvariable=self.total2,
                               foreground="yellow", background="black",
                               borderwidth=5, anchor="e")                                
        self.separ2 = ttk.Separator(self.master, orient=HORIZONTAL)

        self.etiq7.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=20, pady=5)        
        self.separ2.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        

        self.button = tk.Button(
        self.master, text="Ping Test", command=self.on_button)
        self.button.pack()
        
        
        self.text = tk.Text(self.master)
        self.text.config(state=tk.DISABLED)
        self.text.pack(padx=5, pady=5)

        self.text2 = tk.Text(self.master)
        self.text2.config(state=tk.DISABLED)
        self.text2.pack(padx=5, pady=5)
 
    @tk_after
    def button_state(self, enabled=True):
        state = tk.NORMAL
        if not enabled:
            state = tk.DISABLED
        self.button.config(state=state)
 
    @tk_after
    def clear_text(self):
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)
        self.text.config(state=tk.DISABLED)
 
    @tk_after
    def insert_text(self, text):
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END, text)

        self.text.config(state=tk.DISABLED)        
 

    @submit_to_pool_executor(thread_pool_executor)

   
    
    def ping(self):
        self.button_state(False)
        self.clear_text()
        self.insert_text('Starting ping request')

        self.button = tk.Button(
        self.master, total="Calcular", command=self.on_button)
        self.button.pack()
           
     

    def on_button(self):
        self.ping()

        
        self.button = tk.Button(
        self.master, text2="Ping Test", command=self.on_button)
        self.button.pack()

        self.text2 = tk.Text2(self.master)
        self.text2.config(state=tk.DISABLED)
        self.text2.pack(padx=5, pady=5)

      
    @tk_after
    def button_state(self, enabled=True):
        state = tk.NORMAL
        if not enabled:
            state = tk.DISABLED
        self.button.config(state=state)
 
    @tk_after
    def clear_text2(self, text2):
        self.text2.config(state=tk.NORMAL)
        self.text2.delete(1.0, tk.END)
        self.text2.config(state=tk.DISABLED)
 
    @tk_after
    def insert_text2(self, text2):
        self.text2.config(state=tk.NORMAL)
        self.text2.insert(tk.END, text2)
        self.text2.config(state=tk.DISABLED)
   
 
    def on_button(self): 
        self.ping()
 
    @submit_to_pool_executor(thread_pool_executor)
    
    def ping(self):
        self.button_state(False)
        self.clear_text()
        self.insert_text2('Starting ping request')
        
        result = os.popen("ping "+self.entry.get()+" -n 1")
        for line in result:
            self.insert_text(line)

        resultt = os.popen("ping "+self.entry2.get()+" -n 1")
        for line in resultt:
            self.insert_text2(line)

        
        resulttt = os.system("ping -n 1 -w 500 " +self.entry2.get()+ " > nul")
  
        if resulttt == 0:
           self.total2.set("¡OKy!")
        else:
           self.total2.set("¡ERRoR!")
           os.system("communicator1.mp3")
           

        return ping

    def sonido_alerta():
        os.system("communicator1.mp3")

        archivo_servidores = open('servidores.csv')
        servidores_reader = csv.reader(archivo_servidores)
        datos_servidores = list(servidores_reader)

        contador = 0
 
        while True:
         for i in range(len(datos_servidores)):
          servidorTexto = datos_servidores[i][0]
          servidorIP = datos_servidores[i][1]
          resultado = ping(datos_servidores[i][1])


        self.total2.set("{0:30} {1:17} {2:7}".format(
                Fore.WHITE + servidorTexto, servidorIP, Fore.RED + resultado))
        sonido_alerta()

        self.total2.set()

        time.sleep(10)


        self.insert_text('ping request finished')

        self.button_state(True)


     
if __name__ == '__main__':
     app = tk.Tk()
     main_frame = MainFrame()
     app.mainloop()
     



