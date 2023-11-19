import tkinter as tk
import json
import os
import subprocess

# Cargar programas adicionales
#proceso_blufor = subprocess.Popen(['python', 'baraja_blufor.py'])
#proceso_opfor = subprocess.Popen(['python', 'baraja_opfor.py'])
proceso_compukill = subprocess.Popen(['python', 'combat_calculator.py'])
proceso_rules = subprocess.Popen(['python', 'rules.py'])
proceso_ipc = subprocess.Popen(['python', 'ipc_count.py'])
proceso_notes = subprocess.Popen(['python', 'notes.py'])

ventana = tk.Tk()
ventana.title("Axis_of_Conquest_1933_v0.1")

ANCHO, ALTO = 1000, 800
ventana.geometry(f"{ANCHO}x{ALTO}")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scroll_x = tk.Scrollbar(ventana, orient=tk.HORIZONTAL, command=canvas.xview)
#scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
scroll_y = tk.Scrollbar(ventana, orient=tk.VERTICAL, command=canvas.yview)
#scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

mapa = tk.PhotoImage(file='mapa.png')
canvas.create_image(0, 0, anchor=tk.NW, image=mapa)

# Obtener la lista de nombres de archivo en el directorio "fichas"
opfor_files = [f for f in os.listdir('fichas') if os.path.isfile(os.path.join('fichas', f))]

# Cargar las imágenes de OPFOR desde el directorio "fichas"
opfor_fichas = [tk.PhotoImage(file=os.path.join('fichas', ficha)) for ficha in opfor_files]

# Obtener la lista de nombres de archivo en el directorio "fichas_b"
blufor_files = sorted([f for f in os.listdir('fichas_b') if os.path.isfile(os.path.join('fichas_b', f))])

# Cargar las imágenes de BLUFOR desde el directorio "fichas_b"
blufor_fichas = [tk.PhotoImage(file=os.path.join('fichas_b', ficha)) for ficha in blufor_files]

opfor = [canvas.create_image(100, 1000, anchor=tk.NW, image=ficha) for ficha in opfor_fichas]
blufor = [canvas.create_image(3744, 937, anchor=tk.NW, image=ficha) for ficha in blufor_fichas]

arrastrando = None
offset_x, offset_y = 0, 0

import tkinter as tk
import json
import os
import subprocess

# ... (resto del código)

arrastrando = None
fichas_seleccionadas = []  # Nueva variable para el seguimiento de fichas seleccionadas
offset_x, offset_y = 0, 0

def iniciar_arrastre(evento):
    global arrastrando, offset_x, offset_y, fichas_seleccionadas
    x, y = canvas.canvasx(evento.x), canvas.canvasy(evento.y)

    # Verificar si la tecla Shift está presionada
    if evento.state & 0x1:  # 0x1 representa la tecla Shift
        fichas_seleccionadas = []

        # Identificar las fichas en contacto con el punto inicial
        for ficha in opfor + blufor:
            if (canvas.coords(ficha)[0] <= x <= canvas.coords(ficha)[0] + 60 and
                canvas.coords(ficha)[1] <= y <= canvas.coords(ficha)[1] + 60):
                fichas_seleccionadas.append(ficha)

        if fichas_seleccionadas:
            # Actualizar arrastrando solo si hay fichas seleccionadas
            arrastrando = fichas_seleccionadas[0]
            offset_x = x - canvas.coords(arrastrando)[0]
            offset_y = y - canvas.coords(arrastrando)[1]
    else:
        # Proceder como antes si la tecla Shift no está presionada
        for ficha in opfor + blufor:
            if (canvas.coords(ficha)[0] <= x <= canvas.coords(ficha)[0] + 60 and
                canvas.coords(ficha)[1] <= y <= canvas.coords(ficha)[1] + 60):
                arrastrando = ficha
                offset_x = x - canvas.coords(arrastrando)[0]
                offset_y = y - canvas.coords(arrastrando)[1]

def mover_ficha(evento):
    if arrastrando:
        x, y = canvas.canvasx(evento.x), canvas.canvasy(evento.y)
        canvas.coords(arrastrando, x - offset_x, y - offset_y)

        # Mover las demás fichas seleccionadas si la tecla Shift está presionada
        for ficha in fichas_seleccionadas[1:]:
            x_shift, y_shift = canvas.coords(ficha)
            canvas.coords(ficha, x - offset_x, y - offset_y)

def soltar_ficha(evento):
    global arrastrando, fichas_seleccionadas
    arrastrando = None
    fichas_seleccionadas = []

# ... (resto del código)

def iniciar_desplazamiento(evento):
    canvas.scan_mark(evento.x, evento.y)

def desplazar(evento):
    canvas.scan_dragto(evento.x, evento.y, gain=1)

def desplazar_rueda(evento):
    if evento.delta:
        canvas.yview_scroll(int(-1*(evento.delta/120)), "units")

canvas.bind("<Button-1>", iniciar_arrastre)
canvas.bind("<B1-Motion>", mover_ficha)
canvas.bind("<ButtonRelease-1>", soltar_ficha)
canvas.bind("<ButtonPress-2>", iniciar_desplazamiento)
canvas.bind("<B2-Motion>", desplazar)
canvas.bind("<MouseWheel>", desplazar_rueda)

# Función para guardar las posiciones
def guardar_posiciones():
    posiciones = {}

    for i, ficha in enumerate(opfor + blufor):
        x, y = canvas.coords(ficha)
        posiciones[f'ficha_{i}'] = {'x': x, 'y': y}

    ventana_info = {
        'x': ventana.winfo_x(),
        'y': ventana.winfo_y(),
        'width': ventana.winfo_width(),
        'height': ventana.winfo_height()
    }
    posiciones['ventana'] = ventana_info

    with open('posiciones.json', 'w') as archivo:
        json.dump(posiciones, archivo)

    ventana.destroy()
    proceso_compukill.terminate()
    proceso_rules.terminate()
    proceso_ipc.terminate()
    proceso_notes.terminate()


# Función para cargar las posiciones
def cargar_posiciones():
    try:
        with open('posiciones.json', 'r') as archivo:
            posiciones = json.load(archivo)

        for i, ficha in enumerate(opfor + blufor):
            posicion = posiciones.get(f'ficha_{i}')
            if posicion:
                x, y = posicion['x'], posicion['y']
                canvas.coords(ficha, x, y)

        ventana_info = posiciones.get('ventana')
        if ventana_info:
            ventana.geometry(f"{ventana_info['width']}x{ventana_info['height']}+{ventana_info['x']}+{ventana_info['y']}")

    except FileNotFoundError:
        pass

cargar_posiciones()
ventana.protocol("WM_DELETE_WINDOW", guardar_posiciones)

ventana.mainloop()
