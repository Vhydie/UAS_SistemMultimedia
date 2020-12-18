# UAS Nomor 2
# Ciptakan citra dari teks “NIM - Nama lengkap”
# dan berikan juga “tanggal waktu” penciptaan file tersebut.
# Kemudian sisipkan citra tersebut ke dalam foto Anda
# dan tambahkan filter embossing pada gambar tersebut.
# Ini salah satu contoh hasilnya,
# punya Anda lokasi teksnya harus berbeda


# Definition
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import datetime, imageio


# Initialization
# Import image dan mengatur size image agar tetap sama
img_1 = Image.open("Vhydie Gilang Christianto The.jpg").resize((960, 960))
# Mengurus waktu pembuatan citra
date_string = datetime.datetime.now().strftime("%d/%m/%Y  -  %H:%M:%S")
# Pesan yang akan dimasukkan dalam citra
msg_1 = "18218016 - Vhydie Gilang Christianto The\n" + date_string


# Main Code
# Menggambar kembali image
draw1 = ImageDraw.Draw(img_1)
# Mengambil ukuran text
w, h = draw1.textsize(msg_1)
# Menambahkan text dalam image
draw1.rectangle(((w/2)-10, 800, 870, 885), fill='black')
draw1.text((w/2,800), msg_1, fill="white", font = ImageFont.truetype("arial.ttf", 40))
# Menyimpan Image
img_1.save("18218016_Nomor2_Normal.png")
# Membuat Filter Embossing
img_emboss = img_1.filter(ImageFilter.EMBOSS)
# Menyimpan Image Hasil Embossing
img_emboss.save("18218016_Nomor2_Emboss.png")