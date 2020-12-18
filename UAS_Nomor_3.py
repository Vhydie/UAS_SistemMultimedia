# UAS Nomor 3
# Ambil gambar background pemandangan sekitar rumah Anda
# menggunakan smartphone atau apapun.
# Kembali menggunakan Python,
# import gambar pemandangan tersebut
# dan sisipkan teks “Nim - Nama lengkap”
# dan berikan juga “tanggal waktu” penciptaan file tersebut.
# Kemudian kombinasikan hasil gambar tersebut dengan foto Anda (Foreground)
# dengan menggunakan 3 variasi nilai alpha channelyang berbeda, kemudian tampilkan hasilnya.


# Definition
from PIL import Image, ImageDraw, ImageFont
import datetime, imageio


# Initialization
# Import image dan mengatur size image agar tetap sama
# Untuk background yakni pemandangan
background_1 = Image.open("Pemandangan.jpg").resize((960, 960))
background_2 = Image.open("Pemandangan.jpg").resize((960, 960))
background_3 = Image.open("Pemandangan.jpg").resize((960, 960))
# Untuk foreground yakni foto diri
foreground_1 = Image.open("Vhydie Gilang Christianto The.jpg").resize((960, 960))
foreground_2 = Image.open("Vhydie Gilang Christianto The.jpg").resize((960, 960))
foreground_3 = Image.open("Vhydie Gilang Christianto The.jpg").resize((960, 960))
# Mengurus waktu pembuatan citra
date_string = datetime.datetime.now().strftime("%d/%m/%Y  -  %H:%M:%S")
# Pesan yang akan dimasukkan dalam citra
msg = "18218016 - Vhydie Gilang Christianto The\n" + date_string

# Membuat alpha channel
# Untuk alpha 0.2 = 0.2 x 256 = 51.2, dibulatkan jadi 51
alpha_02 = Image.new("L", (960, 960), 51)
# Untuk alpha 0.5 = 0.5 x 256 = 128
alpha_05 = Image.new("L", (960, 960), 128)
# Untuk alpha 0.8 = 0.8 x 256 = 204.8, dibulatkan jadi 205
alpha_08 = Image.new("L", (960, 960), 205)





# Main Code
# Menggambar kembali image
draw_background_1 = ImageDraw.Draw(background_1)
draw_background_2 = ImageDraw.Draw(background_2)
draw_background_3 = ImageDraw.Draw(background_3)
# Mengambil ukuran text
w, h = draw_background_1.textsize(msg)
# Menambahkan text dalam image
draw_background_1.rectangle(((w/2)-10, 800, 870, 885), fill='black')
draw_background_2.rectangle(((w/2)-10, 800, 870, 885), fill='black')
draw_background_3.rectangle(((w/2)-10, 800, 870, 885), fill='black')
draw_background_1.text((w/2,800), msg, fill="red", font = ImageFont.truetype("arial.ttf", 40))
draw_background_2.text((w/2,800), msg, fill="red", font = ImageFont.truetype("arial.ttf", 40))
draw_background_3.text((w/2,800), msg, fill="red", font = ImageFont.truetype("arial.ttf", 40))
# Menyimpan Image Background sebelum ada alpha channel sama sekali
background_1.save("18218016_Nomor3_PemandanganNormal.png")

# Menambahkan alpha channel ke gambar RGB untuk masing-masing gambar
# Untuk kasus pertama, alpha foreground = 0.2, alpha background = 0.8
foreground_1.putalpha(alpha_02)
background_1.putalpha(alpha_08)
# Untuk kasus kedua, alpha foreground = 0.5, alpha background = 0.5
foreground_2.putalpha(alpha_05)
background_2.putalpha(alpha_05)
# Untuk kasus ketiga, alpha foreground = 0.8, alpha background = 0.2
foreground_3.putalpha(alpha_08)
background_3.putalpha(alpha_02)

# Menyatukan Image untuk masing-masing background dan foregorund
# Gambar pertama
img_1 = Image.alpha_composite(background_1, foreground_1)
img_1.save("18218016_Nomor3_Kombinasi1.png")
# Gambar kedua
img_2 = Image.alpha_composite(background_2, foreground_2)
img_2.save("18218016_Nomor3_Kombinasi2.png")
# Gambar ketiga
img_3 = Image.alpha_composite(background_3, foreground_3)
img_3.save("18218016_Nomor3_Kombinasi3.png")