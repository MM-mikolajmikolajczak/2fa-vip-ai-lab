"""Ta sama fałszywa strona, ale logowanie kluczem passkey (prawdziwy podpis ECDSA P-256)."""
import json
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from panel_hakera import odbierz, znacznik

klucz = ec.generate_private_key(ec.SECP256R1())           # klucz prywatny: zostaje w YubiKey / telefonie
dane = json.dumps({"challenge": "8f3a1c", "origin": "https://login-panel-security.local"}).encode()
podpis = klucz.sign(dane, ec.ECDSA(hashes.SHA256()))      # origin wpisała przeglądarka, z paska adresu


def bank(dane, podpis):                                   # bank zna tylko klucz publiczny
    klucz.public_key().verify(podpis, dane, ec.ECDSA(hashes.SHA256()))
    return json.loads(dane)["origin"] == "https://bank.pl"


import time
time.sleep(2.0)
print("\n  Panel serwisowy - logowanie\n  https://login-panel-security.local\n", flush=True)
time.sleep(1.5)
print("  [ Zaloguj kluczem passkey ]", flush=True)
znacznik("zaloguj")
time.sleep(1.0)
print("\n  podpisano dla:\n  " + json.loads(dane)["origin"], flush=True)
time.sleep(1.0)
print("\n  bank: " + ("OK" if bank(dane, podpis) else "ODRZUCONE\n  (podpis jest dla innej domeny)"), flush=True)
time.sleep(1.0)
try:
    bank(dane.replace(b"login-panel-security.local", b"bank.pl"), podpis)     # lustro podmienia origin
except InvalidSignature:
    print("\n  podmiana origin:\n  NIEWAŻNY PODPIS", flush=True)
odbierz("BRAK SESJI:", "91")
odbierz("    bank odrzucił logowanie passkey", "91")
