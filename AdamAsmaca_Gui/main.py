from tkinter import *
from tkinter import messagebox
import random


# Kelimeler
KELIMELER = ["kehribar", "yakamoz", "efsun", "girdap", "zerdali", "sevda", "omur", "kus", "bahar", "hazan"]

# Adam asmaca çizimleri --> hata sayısına göre gösterilir
adam_asmaca_sekli = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",   # 0 hata
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",   # 1 hata
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",   # 2 hata
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",   # 3 hata
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",  # 4 hata
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",  # 5 hata
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="  # 6 hata
]

# Oyun durumu (state)
kelime = random.choice(KELIMELER)          # seçilen gizli kelime
gizli = ["_"] * len(kelime)                # kullanıcıya gösterilen hali
hatalar = 0                                # yanlış tahmin sayısı
tahmin_edilen_harfler = []                 # tekrar girilmesini engellemek için


# Kullanıcı tahmin yaptığında çalışan fonksiyon
def tahmin_et():
    global hatalar

    harf = entry.get().lower().strip()    # inputtan harf al
    entry.delete(0, END)             # inputu temizle

    # Geçersiz giriş kontrolü (boş ya da birden fazla karakter)
    if not harf or len(harf) > 1:
        messagebox.showwarning("Uyarı", "Lütfen bir harf giriniz!")
        return

    # Aynı harf tekrar girilmiş mi kontrolü
    if harf in tahmin_edilen_harfler:
        messagebox.showinfo("Bilgi","Bu harfi zaten denedin!")
        return

    tahmin_edilen_harfler.append(harf)    # harfi listeye ekle

    # Harf kelimede varsa gizliyi güncelle
    if harf in kelime:
        for i in range(len(kelime)):
            if kelime[i] == harf:
                gizli[i] = harf
    else:
        hatalar += 1     # yanlış tahmin --> hata artar

    # UI güncellemeleri
    label_sekil.config(text=adam_asmaca_sekli[hatalar])   # adam çizimi
    label_kelime.config(text=" ".join(gizli))             # kelimenin yeni hali
    label_can.config(text=f"Kalan Can: {6 - hatalar}")    # kalan can

    # Kazanma durumu (artık "_" kalmadıysa)
    if "_" not in gizli:
        messagebox.showinfo("Tebrikler!", f"Kazandınız!🎉 Kelime: {kelime}")
        oyunu_bitir()

    # Kaybetme durumu (hata 6'ya ulaştıysa)
    elif hatalar >= 6:
        label_sekil.config(text=adam_asmaca_sekli[6])  # son çizimi garantiye al
        messagebox.showerror("Oyun Bitti", f"Kaybettiniz! Kelime {kelime}")
        oyunu_bitir()

# Oyun bittiğinde çalışan fonksiyon
def oyunu_bitir():
    entry.config(state="disabled")                 # kullanıcı giriş yapamasın diye
    button.config(state="disabled")                # tahmin butonu pasif
    reset_button.config(state="normal")            # reset butonu aktif olur
    tekrar_basla_label.config(text="Oyun Bitti")   # kullanıcıya bilgi verilir


# Oyunu sıfırlayan fonksiyon (yeni oyun başlatır)
def reset():
    global kelime, gizli, hatalar, tahmin_edilen_harfler

    # Oyun state sıfırlanır
    kelime = random.choice(KELIMELER)
    gizli = ["_"] * len(kelime)
    hatalar = 0
    tahmin_edilen_harfler = []

    # UI sıfırlanır
    label_kelime.config(text=" ".join(gizli))
    label_can.config(text="Kalan Can: 6")
    label_sekil.config(text=adam_asmaca_sekli[0])

    # Input sıfırlanır
    entry.config(state="normal")
    button.config(state="normal")
    entry.focus_set()

    # Reset butonu tekrar kapatılır (oyun devam ediyor çünkü)
    reset_button.config(state="disabled")
    tekrar_basla_label.config(text="")     # "Oyun Bitti" yazısı silinir


# UI
window = Tk()
window.title("Adam Asmaca")
window.minsize(width=400, height=400)

# Adam çizimi label
label_sekil = Label(window, text=adam_asmaca_sekli[0], font=("Courier", 14))
label_sekil.pack(pady=5)

# Kelimeyi gösteren label
label_kelime = Label(window, text=" ".join(gizli), font=("Arial", 20))
label_kelime.pack(pady=10)

# Kullanıcıdan harf alan input
entry = Entry(window, font=("Arial", 14), width=5)
entry.pack(pady=5)
entry.focus_set()

# Tahmin butonu
button = Button(window, text="Tahmin Et", command=tahmin_et)
button.pack(pady=5)

# Oyun durumu yazısı (başta boş)
tekrar_basla_label = Label(window, text="")
tekrar_basla_label.pack(pady=5)

# Oyunu yeniden başlatma butonu
reset_button = Button(window, text="Tekrar Dene",state="disabled",command=reset)
reset_button.pack(pady=5)

# Kalan can label
label_can = Label(window, text=f"Kalan Can: 6", font=("Arial", 12))
label_can.pack(pady=10)

window.mainloop()
