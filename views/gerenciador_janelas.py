import tkinter as tk

class GerenciadorJanelas:
    def __init__(self, root):
        self.root = root
        self.frames = {}

    def adicionar_frame(self, nome, frame_class):
        self.frames[nome] = frame_class(self.root)
        self.frames[nome].grid(row=0, column=0, sticky="nsew")

    def mostrar_frame(self, nome):
        frame = self.frames[nome]
        frame.tkraise()