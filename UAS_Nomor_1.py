# UAS Nomor 1
# Ciptakan citra dari teks “NIM - Nama lengkap” 
# dan berikan juga “tanggal dan waktu” penciptaan file tersebut.
# Kemudian sisipkan citra tersebut ke dalam foto Anda
# dan buatlah menjadi format GIF.
# Ini salah satu contoh hasilnya,
# punya Anda lokasi teksnya harus berbeda.


# Definition
from PIL import Image, ImageDraw, ImageFont
import datetime, imageio


# Initialization
# Import image dan mengatur size image agar tetap sama
imgAsli_1 = Image.open("Vhydie Gilang Christianto The.jpg").resize((960, 960))
img_1 = Image.open("Vhydie Gilang Christianto The.jpg").resize((960, 960))
imgAsli_2 = Image.open("Sistem Multimedia.png").resize((960, 960))
# Membuat image baru dengan latar belakang warna hitam
imgAsli_3 = Image.new('RGB', (960, 960), color = 'black')
img_3_1 = Image.new('RGB', (960, 960), color = 'black')
img_3_2 = Image.new('RGB', (960, 960), color = 'black')
img_3_3 = Image.new('RGB', (960, 960), color = 'black')
# Mengurus waktu pembuatan citra
date_string = datetime.datetime.now().strftime("%d/%m/%Y  -  %H:%M:%S")
# Pesan yang akan dimasukkan dalam citra
msg_1 = "18218016 - Vhydie Gilang Christianto The\n" + date_string
msg_2 = "Terima kasih\ntelah mengajar selama 1 semester ini"
msg_3 = "Sehat selalu\nPak Yusep, Kang Rizki, Teh Chessa!"


# Main Code
# Menggambar kembali image
draw1 = ImageDraw.Draw(img_1)
draw3_1 = ImageDraw.Draw(img_3_1)
draw3_2 = ImageDraw.Draw(img_3_2)
draw3_3 = ImageDraw.Draw(img_3_3)
# Mengambil ukuran text
w, h = draw1.textsize(msg_1)
# Menambahkan text dalam image
draw1.rectangle(((w/2)-10, 800, 870, 885), fill='black')
draw1.text((w/2,800), msg_1, fill="white", font = ImageFont.truetype("arial.ttf", 40))
draw3_1.text((w/2,240), msg_1, fill="white", font = ImageFont.truetype("arial.ttf", 40))
draw3_2.text((w/2,360), msg_2, fill="white", font = ImageFont.truetype("arial.ttf", 40))
draw3_3.text((w/2,480), msg_3, fill="white", font = ImageFont.truetype("arial.ttf", 40))
# Memasukkan image dalam list yang akan ditampilkan
images = [imgAsli_2, imgAsli_2, imgAsli_1, img_1, imgAsli_3, img_3_1, img_3_2, img_3_3]
# Mengeluarkan dan menghasilkan GIF
imageio.mimsave('18218016_Nomor1.GIF', images, duration = 0.7, loop = 0)