import random

<<<<<<< HEAD
adam_asmaca_sekli = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
]


def adam_asmaca():
    kelime_bankasi = ["kehribar", "yakamoz", "efsun", "girdap", "zerdali", "sevda", "omur", "kus", "bahar", "hazan"]

    kelime = random.choice(kelime_bankasi)
    tahmin_edilen_harfler = []
    can_sayisi = 6
    kelime_uzunlugu = ['_'] * len(kelime)

    print("Adam Asmaca Oyununa Hoş Geldiniz!")

    while can_sayisi > 0:
        print(adam_asmaca_sekli[6 - can_sayisi])
        print("\nGüncel kelime: " + ' '.join(kelime_uzunlugu))
        print(f"Kalan Can Sayısı: {can_sayisi}")

        tahmin = input("Bir harf tahmin et: ").lower()

        if not tahmin.isalpha() or len(tahmin) != 1:
            print("Lütfen sadece bir harf girin!")
            continue

        if tahmin in tahmin_edilen_harfler:
            print("Bu harfi zaten denedin!")
            continue
        tahmin_edilen_harfler.append(tahmin)

        if tahmin in kelime:
            for i in range(len(kelime)):
                if kelime[i] == tahmin:
                    kelime_uzunlugu[i] = tahmin
            print("Şanslı tahmin!🎉")
        else:
            can_sayisi -= 1
            print(f"Yanlış! Kalan can sayısı: {can_sayisi}")

    if '_' in kelime_uzunlugu:
        print(f"\nTebrikler🎉 kelimeyi buldun: {kelime}")
    else:
        print(adam_asmaca_sekli[6])
        print(f"\nKaybettiniz! Kelime şuydu: {kelime}")

if __name__ == "__main__":
    adam_asmaca()






=======
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
>>>>>>> 825bf3be65ed5daebd3c8d18b53f3b044dfed1e4

