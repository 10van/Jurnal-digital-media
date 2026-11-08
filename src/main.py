import tkinter as tk
from gui import creare_formular

def main():
    root = tk.Tk()
    root.title("Jurnal Digital Media")
    root.geometry("400x350")

    # Aducem formularul pe fereastra principală
    formular = creare_formular(root)
    formular.pack(fill="both", expand=True)

    # Menține fereastra deschisă
    root.mainloop()

if __name__ == "__main__":
    main()