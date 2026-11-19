"""OKNO HAKERA (symulacja). Bez sieci: "przechwycone" dane to wpisy w lokalnym pliku."""
import os
import time

SKRZYNKA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skrzynka_hakera.log")


def znacznik(nazwa):                             # w filmie: czas zdarzenia do montażu; w paczce nic nie robi
    pass


def odbierz(tekst, kolor="92"):                  # wołają to symulacje po stronie ofiary
    znacznik("haker " + tekst[:20])
    with open(SKRZYNKA, "a", encoding="utf-8") as f:
        f.write(f"{kolor}|{tekst}\n")


if __name__ == "__main__":
    open(SKRZYNKA, "w").close()
    print("[*] nasłuchuję... czekam na ruch ofiary", flush=True)
    with open(SKRZYNKA, encoding="utf-8") as f:
        while True:
            linia = f.readline()
            if not linia:
                time.sleep(0.05)
                continue
            kolor, tekst = linia.rstrip("\n").split("|", 1)
            znak, kolor = ("-", "91") if kolor == "31" else ("+", kolor)
            print(f"\033[{kolor}m[{znak}] {tekst}\033[0m", flush=True)
