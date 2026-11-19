"""SYMULACJA Device Code, bez sieci. Lewe okno = prezes; prawe okno (panel_hakera.py) = haker.
Kolejność jak w filmie: skrypt hakera prosi dostawcę o kod, prezes wpisuje go na oficjalnej stronie,
haker dostaje tokeny. Nic nie łączy się z siecią - "dostawca" to tylko komunikaty."""
import secrets
import time

from panel_hakera import odbierz, znacznik

KOD = "VIP9-8841"
time.sleep(2.0)                                          # okno hakera już nasłuchuje

odbierz("skrypt -> dostawca:", "95")
odbierz("    jestem nowym urządzeniem, daj kod", "95")
time.sleep(0.8)
odbierz(f"kod urządzenia: {KOD}", "95")
odbierz("    (podsyłam go prezesowi)", "95")

time.sleep(1.0)
print("\n  Prezes: oficjalna strona dostawcy\n  (zalogowany kluczem passkey)\n", flush=True)
time.sleep(1.0)
print(f"  kod z zaproszenia: {KOD}\n", flush=True)
time.sleep(2.5)
print("  [ Zatwierdź ]", flush=True)
znacznik("zatwierdz")
time.sleep(0.6)

odbierz("PRZEJĘTO KONTO PREZESA:", "91")
odbierz(f"    access_token={secrets.token_hex(6)}", "91")
odbierz(f"    refresh_token={secrets.token_hex(6)}", "91")
print("\n  Zatwierdzono.", flush=True)
