import tkinter as tk

# Lista de nombres de las imágenes
imagenes = ['rules_1.png', 'rules_2.png', 'rules_3.png']

# Función para ir a la imagen siguiente
def adelante():
    global indice_imagen
    if indice_imagen < len(imagenes) - 1:
        indice_imagen += 1
        mostrar_imagen()

# Función para ir a la imagen anterior
def atras():
    global indice_imagen
    if indice_imagen > 0:
        indice_imagen -= 1
        mostrar_imagen()

# Función para mostrar la imagen actual
def mostrar_imagen():
    imagen_path = imagenes[indice_imagen]
    imagen = tk.PhotoImage(file=imagen_path)
    etiqueta.config(image=imagen)
    etiqueta.image = imagen

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Visor de Imágenes")

# Etiqueta para mostrar la imagen
etiqueta = tk.Label(ventana)
etiqueta.pack(pady=10)

# Botones para navegar entre imágenes
boton_atras = tk.Button(ventana, text="Atrás", command=atras)
boton_atras.pack(side=tk.LEFT, padx=10)

boton_adelante = tk.Button(ventana, text="Adelante", command=adelante)
boton_adelante.pack(side=tk.RIGHT, padx=10)

# Inicialización
indice_imagen = 0
mostrar_imagen()

# Iniciar la aplicación
ventana.mainloop()
