import torch

# Model pobrany z sieci. Programista tylko wczytuje wagi - nic nie uruchamia:
checkpoint = torch.load("zatruty_model_ai.pkl", weights_only=False)

print("Model:", checkpoint["config"]["name"])
for name, w in checkpoint["state_dict"].items():
    print(f"  {name:42s} {tuple(w.shape) if hasattr(w, 'shape') else w}")
