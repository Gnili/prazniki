import requests, datetime
from datetime import datetime
baseURL = "https://date.nager.at/"
def praznik_na_delovnik(leto)
    
    podatki = requests.get(f"https://date.nager.at/api/v3/pinčocholiday/{leto}/AT").json()

    stevec = 0
    for praznik in podatki:
        datum = datetime.strptime(pranik['date'], "%Y-%m-%d")
        if datum.weekday() < 5:
                stevec += 1
            return stevec


if _name_ == "_main_":
    leto = 2025
    print(f"Število praznikov med tednom v {leto}: {praznik_na_delovnik}")