

import tkinter as tk
from tkinter import ttk
import random

# Diccionario de unidades y sus stats
unidades = {
    "ACORAZADO": {"ataque": 4, "defensa": 4},
    "PORTAAVIONES": {"ataque": 0, "defensa": 2},
    "CRUCERO": {"ataque": 3, "defensa": 3},
    "DESTRUCTOR": {"ataque": 2, "defensa": 2},
    "SUBMARINO": {"ataque": 2, "defensa": 1},
    "TRANSPORTE": {"ataque": 0, "defensa": 0},
    "CAZA": {"ataque": 3, "defensa": 4},
    "BOMBARDERO TÁCTICO": {"ataque": 3, "defensa": 3},
    "BOMBARDERO ESTRATEGICO": {"ataque": 4, "defensa": 1},
    "AVION DE TRANSPORTE": {"ataque": 0, "defensa": 0},
    "REGIMIENTO DE TANQUES": {"ataque": 3, "defensa": 3},
    "REGIMIENTO DE INF. MECANIZADA": {"ataque": 1, "defensa": 2},
    "REGIMIENTO PARACAIDISTA": {"ataque": 1, "defensa": 2},
    "REGIMIENTO DE INFANTERIA": {"ataque": 1, "defensa": 2},
    "BATERIA DE ARTILLERIA": {"ataque": 2, "defensa": 2},
    "AAA": {"ataque": 0, "defensa": 1},
    "FABRICA": {"ataque": 0, "defensa": 1},
    "BASE AEREA": {"ataque": 0, "defensa": 1},
    "BASE NAVAL": {"ataque": 0, "defensa": 1}
} 

# Lista de bonus
bonus = [
    {
        "condicion": ["REGIMIENTO DE INFANTERIA", "BATERIA DE ARTILLERIA"],
        "mensaje": "Bonus: El factor de ataque de una unidad de infantería aumenta a 2 por cada batería de artillería presente."
    },
    {
        "condicion": ["REGIMIENTO DE INF. MECANIZADA", "BATERIA DE ARTILLERIA"],
        "mensaje": "Bonus: El factor de ataque de una unidad de infantería aumenta a 2 por cada batería de artillería presente."
    },
    {
        "condicion": ["REGIMIENTO PARACAIDISTA", "BATERIA DE ARTILLERIA"],
        "mensaje": "Bonus: El factor de ataque de una unidad paracaidista aumenta a 2 por cada batería de artillería presente."
    },
    {
        "condicion": ["REGIMIENTO DE TANQUES", "BOMBARDERO TÁCTICO"],
        "mensaje": "Bonus: El factor de ataque de un bombardero tactico aumenta a 4 por cada regimiento de tanques presente."
    },
    {
        "condicion": ["BOMBARDERO TÁCTICO", "CAZA"],
        "mensaje": "Bonus: El factor de ataque de un bombardero tactico aumenta a 4 por cada ala de cazas presente."
    },    
    {
        "condicion": ["BOMBARDERO TÁCTICO", "DESTRUCTOR"],
        "mensaje": "Bonus: La presencia de un destructor permire ataques aereos contra submarinos."
    },  
    {
        "condicion": ["BOMBARDERO ESTRATEGICO", "DESTRUCTOR"],
        "mensaje": "Bonus: La presencia de un destructor permire ataques aereos contra submarinos."
    },
    {
        "condicion": ["CAZA", "DESTRUCTOR"],
        "mensaje": "Bonus: La presencia de un destructor permire ataques aereos contra submarinos."
    },
    
    # Agrega más bonus según sea necesario
]

def calcular_tiradas():
    resultados_atacantes = []
    resultados_defensores = []

    for atacante in atacantes:
        unidad_seleccionada = atacante.get()
        if unidad_seleccionada:
            valor_ataque = unidades[unidad_seleccionada]["ataque"]
            resultado_tirada = random.randint(1, 6)
            resultados_atacantes.append((unidad_seleccionada, valor_ataque, resultado_tirada))

    for defensor in defensores:
        unidad_seleccionada = defensor.get()
        if unidad_seleccionada:
            valor_defensa = unidades[unidad_seleccionada]["defensa"]
            resultado_tirada = random.randint(1, 6)
            resultados_defensores.append((unidad_seleccionada, valor_defensa, resultado_tirada))

    for bono in bonus:
        unidades_presentes = set()
        for atacante in atacantes:
            unidad_seleccionada = atacante.get()
            if unidad_seleccionada in bono["condicion"]:
                unidades_presentes.add(unidad_seleccionada)

        if len(unidades_presentes) == len(bono["condicion"]):
            mostrar_mensaje_bonus(bono["mensaje"])

    mostrar_resultados(resultados_atacantes, resultados_defensores)


def mostrar_resultados(resultados_atacantes, resultados_defensores):
    resultado_atacantes_label.config(text="Resultados Atacantes:")
    resultado_defensores_label.config(text="Resultados Defensores:")

    for unidad, valor, tirada in resultados_atacantes:
        resultado_atacantes_label.config(text=resultado_atacantes_label.cget("text") + f"\n{unidad}: Valor de Ataque: {valor}, Resultado de Tirada: {tirada}")

    for unidad, valor, tirada in resultados_defensores:
        resultado_defensores_label.config(text=resultado_defensores_label.cget("text") + f"\n{unidad}: Valor de Defensa: {valor}, Resultado de Tirada: {tirada}")


def limpiar_menus():
    for atacante in atacantes:
        atacante.set('')
    for defensor in defensores:
        defensor.set('')
    resultado_atacantes_label.config(text="Resultados Atacantes:")
    resultado_defensores_label.config(text="Resultados Defensores:")

def mostrar_mensaje_bonus(mensaje):
    popup = tk.Toplevel(ventana)
    label = ttk.Label(popup, text=mensaje)
    label.pack(padx=10, pady=10)
    button = ttk.Button(popup, text="OK", command=popup.destroy)
    button.pack(pady=10)

ventana = tk.Tk()
# Crear marco
marco = ttk.Frame(ventana)
marco.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


# Atacantes
atacantes_label = ttk.Label(marco, text="ATACANTES:")
atacantes_label.grid(row=0, column=0, pady=(0,5))

atacantes = []
for i in range(20):
    atacante_menu = tk.StringVar(ventana, value='')
    atacantes.append(atacante_menu)
    atacante_dropdown = ttk.OptionMenu(marco, atacante_menu, *['']+list(unidades.keys()))
    atacante_dropdown.grid(row=i+1, column=0, pady=(0,2))

# Defensores
defensores_label = ttk.Label(marco, text="DEFENSORES:")
defensores_label.grid(row=0, column=1, pady=(0,5))

defensores = []
for i in range(20):
    defensor_menu = tk.StringVar(ventana, value='')
    defensores.append(defensor_menu)
    defensor_dropdown = ttk.OptionMenu(marco, defensor_menu, *['']+list(unidades.keys()))
    defensor_dropdown.grid(row=i+1, column=1, pady=(0,2))

# Botones
botones_frame = ttk.Frame(marco)
botones_frame.grid(row=24, column=0, columnspan=2, pady=(10,0))

calcular_button = ttk.Button(botones_frame, text="Calcular Tiradas", command=calcular_tiradas)
calcular_button.grid(row=0, column=0, padx=5)

limpiar_button = ttk.Button(botones_frame, text="Limpiar Menús", command=limpiar_menus)
limpiar_button.grid(row=0, column=1, padx=5)

# Resultados
resultado_atacantes_label = ttk.Label(marco, text="Resultados Atacantes:")
resultado_atacantes_label.grid(row=25, column=0, columnspan=2, pady=(10,5))

resultado_defensores_label = ttk.Label(marco, text="Resultados Defensores:")
resultado_defensores_label.grid(row=26, column=0, columnspan=2, pady=(0,10))

# Ajustar expansión de las columnas y filas
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)
marco.grid_columnconfigure((0,1), weight=1)

# Iniciar bucle de eventos
ventana.mainloop()
