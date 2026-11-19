import base64, hashlib, hmac, struct, time

SEKRET = "JBSWY3DPEHPK3PXP"        # ten sam klucz ma telefon i serwer (był w kodzie QR)


def totp(sekret, czas):
    okno = int(czas) // 30                                            # 30-sekundowe okienko
    skrot = hmac.new(base64.b32decode(sekret), struct.pack(">Q", okno), hashlib.sha1).digest()
    o = skrot[-1] & 0x0F
    return f"{(struct.unpack('>I', skrot[o:o + 4])[0] & 0x7FFFFFFF) % 1_000_000:06d}"   # 6 cyfr


if __name__ == "__main__":
    teraz = time.time()
    print("telefon (bez internetu):", totp(SEKRET, teraz))
    print("serwer:                 ", totp(SEKRET, teraz))
    print("adres strony w tym równaniu: BRAK")
