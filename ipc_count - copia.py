import tkinter as tk
from tkinter import messagebox
import json

turn_counter_player1 = 0
turn_counter_player2 = 0

def save_ipc_stats():
    ipc_stats = {
        "turn_counter_player1": turn_counter_player1,
        "turn_counter_player2": turn_counter_player2,
        "total_ipc_player1": entry_total_ipc_player1.get(),
        "used_ipc_player1": entry_used_ipc_player1.get(),
        "ipc_production_player1": entry_ipc_production_player1.get(),
        "total_ipc_player2": entry_total_ipc_player2.get(),
        "used_ipc_player2": entry_used_ipc_player2.get(),
        "ipc_production_player2": entry_ipc_production_player2.get()
    }

    with open("ipc_stats.json", "w") as json_file:
        json.dump(ipc_stats, json_file)

def load_ipc_stats():
    try:
        with open("ipc_stats.json", "r") as json_file:
            ipc_stats = json.load(json_file)

            global turn_counter_player1, turn_counter_player2
            turn_counter_player1 = ipc_stats.get("turn_counter_player1", 0)
            turn_counter_player2 = ipc_stats.get("turn_counter_player2", 0)

            entry_total_ipc_player1.delete(0, tk.END)
            entry_total_ipc_player1.insert(0, ipc_stats.get("total_ipc_player1", "0"))

            entry_used_ipc_player1.delete(0, tk.END)
            entry_used_ipc_player1.insert(0, ipc_stats.get("used_ipc_player1", "0"))

            entry_ipc_production_player1.delete(0, tk.END)
            entry_ipc_production_player1.insert(0, ipc_stats.get("ipc_production_player1", "0"))

            entry_total_ipc_player2.delete(0, tk.END)
            entry_total_ipc_player2.insert(0, ipc_stats.get("total_ipc_player2", "0"))

            entry_used_ipc_player2.delete(0, tk.END)
            entry_used_ipc_player2.insert(0, ipc_stats.get("used_ipc_player2", "0"))

            entry_ipc_production_player2.delete(0, tk.END)
            entry_ipc_production_player2.insert(0, ipc_stats.get("ipc_production_player2", "0"))

    except FileNotFoundError:
        pass

def next_turn_player1():
    global turn_counter_player1
    turn_counter_player1 += 1

    ipc_production_player1_str = entry_ipc_production_player1.get()
    
    if ipc_production_player1_str:
        ipc_production_player1 = int(ipc_production_player1_str)

        total_ipc_player1_str = entry_total_ipc_player1.get()
        if total_ipc_player1_str:
            total_ipc_player1 = int(total_ipc_player1_str)
            total_ipc_player1 += ipc_production_player1

            entry_total_ipc_player1.delete(0, tk.END)
            entry_total_ipc_player1.insert(0, str(total_ipc_player1))

        label_turn_player1.config(text=f"Turn Player 1: {turn_counter_player1}")

    save_ipc_stats()

def next_turn_player2():
    global turn_counter_player2
    turn_counter_player2 += 1

    ipc_production_player2_str = entry_ipc_production_player2.get()
    
    if ipc_production_player2_str:
        ipc_production_player2 = int(ipc_production_player2_str)

        total_ipc_player2_str = entry_total_ipc_player2.get()
        if total_ipc_player2_str:
            total_ipc_player2 = int(total_ipc_player2_str)
            total_ipc_player2 += ipc_production_player2

            entry_total_ipc_player2.delete(0, tk.END)
            entry_total_ipc_player2.insert(0, str(total_ipc_player2))

        label_turn_player2.config(text=f"Turn Player 2: {turn_counter_player2}")

    save_ipc_stats()

def purchase_player1():
    used_ipc_player1_str = entry_used_ipc_player1.get()
    total_ipc_player1_str = entry_total_ipc_player1.get()
    
    if used_ipc_player1_str and total_ipc_player1_str:
        used_ipc_player1 = int(used_ipc_player1_str)
        total_ipc_player1 = int(total_ipc_player1_str)

        if used_ipc_player1 <= total_ipc_player1:
            total_ipc_player1_result = total_ipc_player1 - used_ipc_player1
            entry_total_ipc_player1.delete(0, tk.END)
            entry_total_ipc_player1.insert(0, str(total_ipc_player1_result))
            
            entry_used_ipc_player1.delete(0, tk.END)
            entry_used_ipc_player1.insert(0, "0")
        else:
            messagebox.showerror("Error", "Used IPC cannot be greater than Total IPC")

    save_ipc_stats()

def purchase_player2():
    used_ipc_player2_str = entry_used_ipc_player2.get()
    total_ipc_player2_str = entry_total_ipc_player2.get()
    
    if used_ipc_player2_str and total_ipc_player2_str:
        used_ipc_player2 = int(used_ipc_player2_str)
        total_ipc_player2 = int(total_ipc_player2_str)

        if used_ipc_player2 <= total_ipc_player2:
            total_ipc_player2_result = total_ipc_player2 - used_ipc_player2
            entry_total_ipc_player2.delete(0, tk.END)
            entry_total_ipc_player2.insert(0, str(total_ipc_player2_result))
            
            entry_used_ipc_player2.delete(0, tk.END)
            entry_used_ipc_player2.insert(0, "0")
        else:
            messagebox.showerror("Error", "Used IPC cannot be greater than Total IPC")

    save_ipc_stats()

window = tk.Tk()
window.title("IPC")


# Labels and entry fields for Player 1
label_player1 = tk.Label(window, text="Player 1")
label_player1.grid(row=0, column=0, padx=10, pady=5)

label_total_ipc_player1 = tk.Label(window, text="Total IPC:")
label_total_ipc_player1.grid(row=1, column=0, padx=10, pady=5)

entry_total_ipc_player1 = tk.Entry(window)
entry_total_ipc_player1.grid(row=1, column=1, padx=10, pady=5)

label_used_ipc_player1 = tk.Label(window, text="Used IPC:")
label_used_ipc_player1.grid(row=2, column=0, padx=10, pady=5)

entry_used_ipc_player1 = tk.Entry(window)
entry_used_ipc_player1.grid(row=2, column=1, padx=10, pady=5)
entry_used_ipc_player1.insert(0, "0")

label_ipc_production_player1 = tk.Label(window, text="IPC Production:")
label_ipc_production_player1.grid(row=3, column=0, padx=10, pady=5)

entry_ipc_production_player1 = tk.Entry(window)
entry_ipc_production_player1.grid(row=3, column=1, padx=10, pady=5)
entry_ipc_production_player1.insert(0, "0")

# Labels and entry fields for Player 2
label_player2 = tk.Label(window, text="Player 2")
label_player2.grid(row=0, column=2, padx=10, pady=5)

label_total_ipc_player2 = tk.Label(window, text="Total IPC:")
label_total_ipc_player2.grid(row=1, column=2, padx=10, pady=5)

entry_total_ipc_player2 = tk.Entry(window)
entry_total_ipc_player2.grid(row=1, column=3, padx=10, pady=5)

label_used_ipc_player2 = tk.Label(window, text="Used IPC:")
label_used_ipc_player2.grid(row=2, column=2, padx=10, pady=5)

entry_used_ipc_player2 = tk.Entry(window)
entry_used_ipc_player2.grid(row=2, column=3, padx=10, pady=5)
entry_used_ipc_player2.insert(0, "0")

label_ipc_production_player2 = tk.Label(window, text="IPC Production:")
label_ipc_production_player2.grid(row=3, column=2, padx=10, pady=5)

entry_ipc_production_player2 = tk.Entry(window)
entry_ipc_production_player2.grid(row=3, column=3, padx=10, pady=5)
entry_ipc_production_player2.insert(0, "0")

# "Next Turn" buttons for Player 1 and Player 2
button_next_turn_player1 = tk.Button(window, text="Next Turn Player 1", command=next_turn_player1)
button_next_turn_player1.grid(row=6, column=0, columnspan=2, pady=10)

label_turn_player1 = tk.Label(window, text="Turn Player 1: 0")
label_turn_player1.grid(row=5, column=0, columnspan=2, pady=10)

button_next_turn_player2 = tk.Button(window, text="Next Turn Player 2", command=next_turn_player2)
button_next_turn_player2.grid(row=6, column=2, columnspan=2, pady=10)

label_turn_player2 = tk.Label(window, text="Turn Player 2: 0")
label_turn_player2.grid(row=5, column=2, columnspan=2, pady=10)


# "Purchase" buttons for Player 1 and Player 2
button_purchase_player1 = tk.Button(window, text="Purchase Player 1", command=purchase_player1)
button_purchase_player1.grid(row=4, column=0, columnspan=2, pady=10)

button_purchase_player2 = tk.Button(window, text="Purchase Player 2", command=purchase_player2)
button_purchase_player2.grid(row=4, column=2, columnspan=2, pady=10)

load_ipc_stats()  # Llamada a la función de carga al iniciar la aplicación

window.mainloop()
