import random


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

