import tkinter as tk
from tkinter import ttk, messagebox
from models import TIPURI, valideaza, Recenzie
from storage import salveaza_recenzie


def creare_formular(parinte):
    frame = tk.Frame(parinte, padx=20, pady=20)

    # Elemente grafic
    tk.Label(frame, text="Tip Media:").grid(row=0, column=0, sticky="w")
    combo_tip = ttk.Combobox(frame, values=TIPURI, state="readonly")
    combo_tip.grid(row=0, column=1, pady=5)
    combo_tip.set("Selectați tipul")

    tk.Label(frame, text="Titlu:").grid(row=1, column=0, sticky="w")
    entry_titlu = tk.Entry(frame, width=30)
    entry_titlu.grid(row=1, column=1, pady=5)

    tk.Label(self, text="Realizat de:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    self.entry_made_by = tk.Entry(self, width=40)
    self.entry_made_by.grid(row=2, column=1, sticky="w", padx=10, pady=5)

    tk.Label(frame, text="Rating (1-5):").grid(row=3, column=0, sticky="w")
    spin_rating = tk.Spinbox(frame, from_=1, to=5, width=5)
    spin_rating.grid(row=2, column=1, sticky="w", pady=5)

    tk.Label(frame, text="Review (opțional):").grid(row=4, column=0, sticky="nw")
    text_review = tk.Text(frame, width=30, height=5)
    text_review.grid(row=3, column=1, pady=5)

    # Funcția care se execută când apeși butonul
    def la_salvare():
        tip = combo_tip.get()
        titlu = entry_titlu.get()
        try:
            rating = int(spin_rating.get())
        except ValueError:
            rating = 0
        review = text_review.get("1.0", tk.END).strip()

        # Apelăm funcția de validare
        made_by = self.entry_made_by.get()
        erori = valideaza(tip, titlu, rating, made_by, review)

        if erori:
            messagebox.showerror("Eroare", "\n".join(erori))
        else:
            recenzie_noua = Recenzie(tip, titlu, rating, made_by, review)

            # Salvăm fizic în JSON
            salveaza_recenzie(recenzie_noua)

            messagebox.showinfo("Succes", f"Recenzia a fost salvată cu succes în JSON!")

    tk.Button(frame, text="Salvează Recenzia", command=la_salvare).grid(row=4, column=0, columnspan=2, pady=15)
    return frame