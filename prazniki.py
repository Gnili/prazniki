import requests
import datetime

def praznik_na_delovnik(leto)
    prosti = 0
    klic = requests.get(f"https://date.nager.at/api/v3/publicholidays/{leto}/AT").json()

    
    for k in klic:
        dat = k.get("date").split("-")
        weekday = datetime.datetime(int(dat[0]), int(dat[1]), int(dat[2])).weekday()
        if weekday < 5:
                prosti += 1
            return prosti


if _name_ == "_main_":
    leto = 2025
    print(f"Število praznikov med tednom v {leto}: {praznik_na_delovnik}")