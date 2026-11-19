import pickletools
import sys
import zipfile

# Prześwietla plik modelu rozkaz po rozkazie - BEZ wczytywania go.
RED, GREEN, GREY, END = "\033[91m", "\033[92m", "\033[90m", "\033[0m"
BEZPIECZNE = ("torch", "collections")
plik = sys.argv[1]
with zipfile.ZipFile(plik) as z:                      # plik z torch.save to archiwum z data.pkl w środku
    dane = z.read(next(n for n in z.namelist() if n.endswith("data.pkl")))
n, groźne, czeka = 0, 0, None
for op, arg, pos in pickletools.genops(dane):
    n += 1
    if op.name == "GLOBAL" and not str(arg).startswith(BEZPIECZNE):
        print(RED + f"{pos:6d}  GLOBAL   {arg}   <-- funkcja spoza PyTorcha" + END)
        czeka, groźne = arg, groźne + 1
    elif op.name == "REDUCE" and czeka:
        print(RED + f"{pos:6d}  REDUCE   <-- wywoła ją w chwili wczytania pliku" + END)
        czeka = None
print(GREY + f"\nprzeskanowano {n} rozkazów, model NIE został wczytany" + END)
if groźne:
    print(RED + f"[!] {plik}: ukryty rozkaz wykonywalny. Nie wczytuj!" + END)
else:
    print(GREEN + f"[OK] {plik}: tylko tensory." + END)
