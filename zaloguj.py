"""SYMULACJA bez sieci: "strona" logowania w terminalu. To lustro: dane idą do banku, kopia sesji do hakera."""
import secrets, sys, time
from panel_hakera import odbierz, znacznik
from totp import SEKRET, totp


def pole(etykieta, tekst, ukryj=False, pauza=0.6):
    """pokazuje, jak ofiara wpisuje pole (odtworzenie, nie czyta klawiatury)"""
    print(f"  {etykieta}: ", end="", flush=True)
    time.sleep(pauza)
    znacznik("pole " + etykieta)
    for znak in tekst:
        print("*" if ukryj else znak, end="", flush=True)
        time.sleep(0.075)
    print()
    return tekst


def bank(haslo, kod):                                    # prawdziwy serwer: sprawdza hasło i równanie TOTP
    teraz = time.time()
    if haslo == "Zima2026!" and kod in (totp(SEKRET, teraz), totp(SEKRET, teraz - 30)):
        return "session_id=" + secrets.token_hex(8)      # "opaska na festiwal"


time.sleep(2.0)                                          # okno hakera już nasłuchuje
print("\n  Panel serwisowy - logowanie\n  https://login-panel-security.local\n", flush=True)
time.sleep(1.5)
if "hlk" in sys.argv:                                    # kolejność z filmu po 1:58: hasło, login, kod
    haslo = pole("hasło", "Zima2026!", ukryj=True)
    login = pole("login", "m.mikolajczak@firma.local")
else:
    login = pole("login", "m.mikolajczak@firma.local")
    haslo = pole("hasło", "Zima2026!", ukryj=True)
kod = pole("kod 2FA (z telefonu)", totp(SEKRET, time.time()))
time.sleep(0.8)
print("\n  [ Zaloguj ]", flush=True)
znacznik("zaloguj")
time.sleep(0.7)
sesja = bank(haslo, kod)                                 # lustro przekazuje dane do banku...
if sesja:
    odbierz("PRZECHWYCONO SESJĘ OFIARY:")                # ...i zostawia sobie kopię odpowiedzi
    odbierz("    " + sesja)
    print("\n  Zalogowano.")
else:
    print("\n  Błędne dane.")
