import json
import os


CALE_FISIER = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "recenzii.json"))

def salveaza_recenzie(recenzie_noua):

    os.makedirs(os.path.dirname(CALE_FISIER), exist_ok=True)


    if os.path.exists(CALE_FISIER):
        with open(CALE_FISIER, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []


    from dataclasses import asdict
    data.append(asdict(recenzie_noua))


    with open(CALE_FISIER, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)