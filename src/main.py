import tkinter as tk
from gui import creare_formular

def main():
    root = tk.Tk()
    root.title("Jurnal Digital Media")
    root.geometry("1920x1080")


    formular = creare_formular(root)
    formular.pack(fill="both", expand=True)

    # Menține fereastra deschisă
    root.mainloop()

if __name__ == "__main__":
    main()