import tkinter as tk
from tkinter import ttk

class FormularioBase(tk.Frame):
    def __init__(self, master, campos):
        super().__init__(master)
        self.campos = campos
        self.widgets = {}
        self.criar_formulario()

    def criar_formulario(self):
        for campo in self.campos:
            label = tk.Label(self, text=campo["label"])
            label.pack()
            if campo["tipo"] == "entry":
                widget = tk.Entry(self)
            elif campo["tipo"] == "combobox":
                widget = ttk.Combobox(self, values=campo.get("opcoes", []))
            widget.pack()
            self.widgets[campo["label"]] = widget

    def validar(self):
        raise NotImplementedError("Método validar deve ser implementado nas subclasses.")