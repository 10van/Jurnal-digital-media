from dataclasses import dataclass, asdict

TIPURI = ["Film", "Serial", "Carte", "Joc"]
MAX_CUVINTE = 100

@dataclass
class Recenzie:
    tip: str
    titlu: str
    rating: int
    text: str = ""
    cale_imagine: str = ""

def valideaza(tip, titlu, rating, text=""):
    """Întoarce o listă de erori. Lista goală înseamnă că datele sunt va"""
    erori = []
    if tip not in TIPURI:
        erori.append("Selectați tipul media.")
    if not titlu.strip():
        erori.append("Titlul nu poate fi gol.")
    if not isinstance(rating, int) or not 1 <= rating <= 5:
        erori.append("Ratingul trebuie să fie între 1 și 5.")
    n = len(text.split())
    if n > MAX_CUVINTE:
        erori.append(f"Review-ul are {n} cuvinte (maxim {MAX_CUVINTE}).")
    return erori