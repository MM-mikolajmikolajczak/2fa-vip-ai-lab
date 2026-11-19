import warnings
import torch

warnings.filterwarnings("ignore")

# Ten sam plik, ale z flagą weights_only=True: tylko liczby, zero poleceń.
try:
    model = torch.load("zatruty_model_ai.pkl", weights_only=True)
except Exception as e:
    print("ZABLOKOWANO:", str(e).splitlines()[0])
