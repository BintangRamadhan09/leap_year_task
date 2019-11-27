### No. 1


# Soal Tahun Kabisat


t = int(input('Masukkan Tahun Anda: '))

def kabisat(x):
    if x % 4 == 0:
        out = 'TAHUN KABISAT'
    else:
        if x % 10 == 0:
            out = 'BUKAN TAHUN KABISAT'
        else:
            if x % 4 == 0:
                out = 'TAHUN KABISAT'
            else:
                out = 'BUKAN TAHUN KABISAT'
    return out


hasil = kabisat(t)
print(f'Hasil : {hasil}')