import tkinter as tk
from views.gerenciador_janelas import GerenciadorJanelas

class MainApp:
    def __init__(self, root):
        self.gerenciador = GerenciadorJanelas(root)
        # Adicione frames aqui
        self.gerenciador.mostrar_frame("MenuPrincipal")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()