# De Los Santos Gutierrez Yessica Odet: Colores y nombre del equipo
import mysql.connector
import tkinter as tk
from tkinter import messagebox
import random

# Cadena de conexion - base del equipo 5
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tkinter_302_equipo_5",
    )

numero_secreto = random.randint(1, 20)

# --- CRUD ---
def guardar():
    # Guarda el intento que escribiste
    try:
        intento = int(caja.get())
        if intento > numero_secreto:
            resultado = "muy alto"
        elif intento < numero_secreto:
            resultado = "muy bajo"
        else:
            resultado = "le atinaste"
        con = conectar(); cur = con.cursor()
        cur.execute("INSERT INTO intentos (intento, resultado) VALUES (%s, %s)", (intento, resultado))
        con.commit(); cur.close(); con.close()
        mensaje.set(f"{resultado} - Guardado")
        consultar()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def consultar():
    try:
        con = conectar(); cur = con.cursor()
        cur.execute("SELECT id, intento, resultado FROM intentos")
        filas = cur.fetchall(); cur.close(); con.close()
        lista.delete(0, tk.END)
        for f in filas:
            lista.insert(tk.END, f"{f[0]} | {f[1]} | {f[2]}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def actualizar():
    try:
        sel = lista.get(lista.curselection()).split(" | ")
        con = conectar(); cur = con.cursor()
        cur.execute("UPDATE intentos SET intento=%s WHERE id=%s", (caja.get(), sel[0]))
        con.commit(); cur.close(); con.close()
        consultar()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def eliminar():
    try:
        sel = lista.get(lista.curselection()).split(" | ")
        con = conectar(); cur = con.cursor()
        cur.execute("DELETE FROM intentos WHERE id=%s", (sel[0],))
        con.commit(); cur.close(); con.close()
        consultar()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def probar():
    # Juego: dice muy alto, muy bajo o le atinaste
    try:
        intento = int(caja.get())
    except:
        messagebox.showinfo("Adivina el número", "Escribe un número del 1 al 20")
        return
    if intento > numero_secreto:
        mensaje.set("Muy alto, intenta con uno más bajo")
    elif intento < numero_secreto:
        mensaje.set("Muy bajo, intenta con uno más alto")
    else:
        mensaje.set("¡Le atinaste! ¡Felicidades!")
        messagebox.showinfo("Adivina el número", "¡Le atinaste!")

def otro_numero():
    global numero_secreto
    numero_secreto = random.randint(1, 20)
    caja.delete(0, tk.END)
    mensaje.set("Ya pensé otro número del 1 al 20, ¡adivínalo!")

# De Los Santos Gutierrez Yessica Odet: Colores y nombre del equipo
FONDO = "#FFE4EC"
COLOR_BOTON = "#FF5C8A"
COLOR_TEXTO = "#4A0E2E"
COLOR_CAJA = "#FFF0F5"

ventana = tk.Tk()
ventana.title("Adivina el número - Equipo 5")
ventana.geometry("380x480")
ventana.configure(bg=FONDO)

tk.Label(ventana, text="Adivina el número del 1 al 20", bg=FONDO, fg=COLOR_TEXTO, font=("Arial", 13, "bold")).pack(pady=10)
caja = tk.Entry(ventana, bg=COLOR_CAJA, fg=COLOR_TEXTO, font=("Arial", 14), justify="center", relief="flat")
caja.pack(pady=5)
mensaje = tk.StringVar(); mensaje.set("Ya pensé un número, ¡adivínalo!")
tk.Label(ventana, textvariable=mensaje, bg=FONDO, fg=COLOR_TEXTO, font=("Arial", 11, "bold"), wraplength=320).pack(pady=5)

tk.Button(ventana, text="Probar", command=probar, bg=COLOR_BOTON, fg="white", font=("Arial", 11, "bold"), relief="flat", width=15).pack(pady=4)
tk.Button(ventana, text="Otro número", command=otro_numero, bg=COLOR_BOTON, fg="white", font=("Arial", 11, "bold"), relief="flat", width=15).pack(pady=4)

lista = tk.Listbox(ventana, width=45, bg="white", fg=COLOR_TEXTO, selectbackground=COLOR_BOTON, selectforeground="white", relief="flat")
lista.pack(pady=8)

tk.Button(ventana, text="Guardar", command=guardar, bg=COLOR_BOTON, fg="white", font=("Arial", 10, "bold"), relief="flat", width=15).pack(pady=2)
tk.Button(ventana, text="Consultar", command=consultar, bg=COLOR_BOTON, fg="white", font=("Arial", 10, "bold"), relief="flat", width=15).pack(pady=2)
tk.Button(ventana, text="Actualizar", command=actualizar, bg=COLOR_BOTON, fg="white", font=("Arial", 10, "bold"), relief="flat", width=15).pack(pady=2)
tk.Button(ventana, text="Eliminar", command=eliminar, bg=COLOR_BOTON, fg="white", font=("Arial", 10, "bold"), relief="flat", width=15).pack(pady=2)

ventana.mainloop()


