import sys
import os

# Añadir la carpeta raíz al PYTHONPATH dinámicamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora intenta importar el módulo
from experto_general.base import BaseConocimientos

import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from experto_general.base import BaseConocimientos
from experto_general.entry import Entry
from experto_general.property import Property
from experto_general.response import Response

# Crea una instancia del motor de inferencia
class InterfazConsultarBase:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x400')
        self.root.title('Consultar Base de Conocimientos')

        # Etiqueta principal
        self.lbl_base = tk.Label(self.root, text="Consultar Base de Conocimientos", font=("Helvetica", 18))
        self.lbl_base.pack(side="top", pady=10)

        # Botones de acciones
        self.btn_consultar = tk.Button(self.root, text="Consultar Entradas", width=30, command=self.consultar_base)
        self.btn_consultar.pack(side="top", pady=5)

        self.quit_btn = tk.Button(self.root, text="Salir", fg="red", width=30, command=self.root.quit)
        self.quit_btn.pack(side="bottom", pady=10)

        # Árbol para mostrar las entradas y propiedades
        self.tree = ttk.Treeview(self.root, columns=("Nombre", "Propiedad"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Propiedad", text="Propiedad")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def consultar_base(self):
        """
        Función para consultar la base de conocimientos y llenar el Treeview
        """
        # Limpiar el árbol antes de agregar nuevas entradas
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obtener todas las entradas de la base de conocimientos
        base = BaseConocimientos()

        for entry in base.entries:
            for prop in entry.properties:
                # Insertar cada entrada con su respectiva propiedad en el Treeview
                self.tree.insert("", "end", values=(entry.name, prop.name))

# Función para ejecutar la interfaz gráfica
def main():
    root = tk.Tk()
    app = InterfazConsultarBase(root)
    root.mainloop()

if __name__ == "__main__":
    main()
