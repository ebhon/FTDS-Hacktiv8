name = '<namamu>'
devices = ['laptop', 'smartphone', 'tablet']

def display(nama):
  print(f'halo {nama}!')

def cetak_angka_2_versi_module(ind, *lst):
  '''
  Function ini digunakan untuk mencari indeks angka dari kumpulan list
  indeks angka yang dicari adalah indeks angka yang paling depan
  '''
if len (lst) < ind:
  print(lst[ind])
else:
  print(-1)
