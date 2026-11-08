from src.models import valideaza

def test_titlu_gol_respins():
    assert valideaza("Film", "  ", 4) != []