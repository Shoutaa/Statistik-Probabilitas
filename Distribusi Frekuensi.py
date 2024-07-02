import math

data = [
    27.5, 33.0, 15.0, 44.7, 59.1, 41.5, 50.0, 49.0,
    40.8, 51.1, 47.9, 40.7, 66.3, 42.3, 46.8, 34.5,
    42.1, 29.0, 62.6, 58.5, 61.8, 38.5, 72.3, 58.1,
    23.9, 65.7, 44.8, 69.1, 66.4, 44.7, 59.6, 31.0,
    54.2, 56.8, 47.8, 38.8, 32.0, 43.8, 45.0, 60.5,
]

def hitung_frekuensi(data, tepi_bawah, tepi_atas):
    frekuensi = 0
    for nilai in data:
        if tepi_bawah <= nilai and tepi_atas >= nilai:
            frekuensi += 1
    return frekuensi

print("Nilai Minimal   : ", min(data))
print("Nilai Maksimal  : ", max(data))

R = max(data) - min(data)
print("Range           : ", R)

kelas = 1
while 2 ** kelas < len(data):
    kelas += 1
print("Kelas           : ", kelas)

interval = R / kelas
i_interval = round(interval + 0.05, 1)
print("Interval        : ", i_interval)

tepi_bawah = min(data)
tepi_atas = tepi_bawah + i_interval - 0.11
print("\nRekap Data Dalam Tabel")
print("| {:<10} | {:<10} | {:<10} | {:<10}|".format("tepi_bawah", "tepi_atas", "Frekuensi","Fre_Relatif"))

while tepi_bawah <= max(data):
    frekuensi = hitung_frekuensi(data, tepi_bawah, tepi_atas)
    f_relatif = (frekuensi / len(data)) * 100
    print("| {:<10.1f} | {:<10.1f} | {:<10} | {:<10.1f}%|".format(tepi_bawah, tepi_atas, frekuensi, f_relatif ))
    tepi_bawah = tepi_atas + 0.1
    tepi_atas += i_interval  

tepi_bawah = min(data)
tepi_atas = tepi_bawah + i_interval - 0.11
print("\nHistogram Frekuensi")
print("| {:<10} | {:<10} | {:<10}| {:<10} | {:<10}|".format("tepi_bawah", "tepi_atas","batas_bawah","batas_atas","Frekuensi"))

batas_bawah = min(data) - 0.05
batas_atas = batas_bawah + i_interval
while tepi_bawah <= max(data):
    frekuensi = hitung_frekuensi(data, tepi_bawah, tepi_atas)
    print("| {:<10.1f} | {:<10.1f} | {:<10.2f} | {:<10.2f} | {:<10}|".format(tepi_bawah, tepi_atas,batas_bawah, batas_atas, frekuensi ))
    tepi_bawah = tepi_atas + 0.1
    tepi_atas += i_interval
    batas_bawah = batas_atas
    batas_atas += i_interval

tepi_bawah = min(data)
tepi_atas = tepi_bawah + i_interval - 0.10001
print("\nPoligon Frekuensi")
print("| {:<10} | {:<10} | {:<10}| {:<10}|".format("tepi_bawah", "tepi_atas","nilai tengah","Frekuensi"))
while tepi_bawah <= max(data):
    frekuensi = hitung_frekuensi(data, tepi_bawah, tepi_atas)
    nilai_tengah = (tepi_atas + tepi_bawah)/2
    print("| {:<10.1f} | {:<10.1f} | {:<10.2f} | {:<10} |".format(tepi_bawah, tepi_atas,nilai_tengah, frekuensi ))
    tepi_bawah = tepi_atas + 0.1
    tepi_atas += i_interval
