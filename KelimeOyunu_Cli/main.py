import random

kelime_bankasi = ["elma", "portakal", "kivi", "armut", "çilek", "hindistancevizi"]

kelime = random.choice(kelime_bankasi)

tahmini_kelime = ['_'] * len(kelime)

tahmin_hakki = 10

tahmin_edilenler = []

while tahmin_hakki > 0:
    print("\nGüncel kelime: " + " ".join(tahmini_kelime))

    tahmin = input("Bir harf tahmin et: ").lower()

    if not tahmin.isalpha() or len(tahmin) != 1:
        print("Lütfen sadece bir harf gir!")
        continue

    if tahmin in tahmin_edilenler:
        print("Bu harfi zaten denedin!")
        continue

    tahmin_edilenler.append(tahmin)

    if tahmin in kelime:
        for i in range(len(kelime)):
            if kelime[i] == tahmin:
                tahmini_kelime[i] = tahmin
        print("Şanslı tahmin!🎉")
    else:
        tahmin_hakki -= 1
        print(f"Yanlış tahmin! 😅 Kalan hak: {tahmin_hakki}")

    if '_' not in tahmini_kelime:
        print(f"\nTebrikler 🎉 Kelimeyi tahmin ettin: {kelime}")
        break

if tahmin_hakki == 0 or '_' in tahmini_kelime:
    print(f"\nTahmin hakkın bitti! Kelime: {kelime}")

