'''
================================================
Graded Challenge 1

Nama : Handwitanto Abraham
Batch : RMT-036

Aplikasi ini adalah aplikasi belanja, dimana pengguna dapat melakukan penambahan produk kedalam keranjang belanja, menghapus produk dari keranjang, menampilkan keranjang belanja,
dan menghitung total biaya yang dikeluarkan untuk berbelanja

Fitur : 
- Tambah produk ke dalam keranjang
- Hapus produk dari dalam keranjang
- Melihat isi dari keranjang belanjaan
- Menghitung total biaya dari produk yang akan dibeli
================================================
'''


'''
Class ini berisi objek barang yang memiliki atribut nama produk dan harga produk
'''
class CartItem():
    def __init__(self, produk, harga):
        self.produk = produk
        self.harga = harga

'''
Class ini berisi method yang merupakan fitur-fitur dari aplikasi ini seperti : 
- Menambah produk ke keranjang
- Melihat daftar produk yang ada di keranjang
- Menghapus produk dari keranjang
- Menghitung total harga dari produk yang ada di keranjang
'''
class Shooping():
    def __init__(self, produk_list, harga_item, total_belanja, hapus_item):
        self.produk_list = produk_list
        self.harga_item = harga_item
        self.total_belanja = total_belanja
        self.hapus_item = hapus_item
        
    '''
    Method ini berisi program yang berfungsi untuk menambahkan produk kedalam keranjang. 
    Cara kerja : 
    - Program akan meminta user melakukan input nama produk dan harga produk yang akan disimpan kedalam keranjang
    - Untuk input harga produk, akan dilakukan validasi untuk memastikan nilai yang di input berupa angka
    - Apabila input sudah sesuai, maka akan di tambahkan kedalam "List".
    - Apabila input berhasil, akan muncul notifikasi bahwa produk berhasil dimasukkan kedalam keranjang

    '''
    def beli(self):
        produk = input("Masukkan nama produk : ") 
        produk = produk.capitalize() 
        while True:
            try:
                harga = int(input("Masukkan harga produk : ")) 
            except ValueError:
                print ("harga harus berupa angka!")
                continue
            else:
                break
        self.produk_list.append(CartItem(produk, harga))
        
        print ("~"*50)
        print (f"{produk} berhasil dimasukkan ke keranjang")
        print ("~"*50)
        print ("")
        print ("")
    
    '''
    Method ini berisi program untuk menampilkan produk-produk yang sudah tersimpan di dalam keranjang.
    Cara kerja : 
    - Program akan melihat terlebih dahulu, apakah sudah terdapat produk di dalam keranjang.
    - Jika belum ada produk, akan menampilkan notifikasi bahwa "Belum ada produk di keranjang"
    - Jika sudah ada produk, sistem akan melakukan looping dengan menghitung jumlah produk yang tersimpan
    - Untuk setiap putaran looping, program akan menampilkan nama produk dan harganya, sehingga tampilan daftar produk tersusun secara rapih.
    '''
    def lihat(self):
        if not self.produk_list:
            print ("Belum ada produk di keranjang")
        else : 
            print ("~"*50)
            print ("Produk di Keranjang")
            print ("~"*50)
            i = 0
            for data in self.produk_list:
                print (f"{i+1}. {data.produk} - Rp. {data.harga},-")
            print ("")
            print ("")

    '''
    Method ini berisi program untuk menghitung total harga dari produk yang tersimpan di dalam keranjang.
    Cara kerja : 
    - Ketika program dijalankan, secara default program membuat variabel "harga_item" dan "total_belanja" yang bernilai 0. Variabel ini digunakan untuk penyimpanan data harga produk
        pada list secara bergantian menggunakan looping
    - Selanjutnya sistem akan melakukan looping berdasarkan jumlah produk yang ada di dalam keranjang.
    - variabel "harga_item" akan mengambil harga dari produk yang ada di keranjang untuk setiap index pada proses looping
    - variabel "total_belanja" kemudian memasukkan nilai dari "harga_item" dan ditambahkan dengan nilai dari "total_belanja" itu sendiri, sehingga di akhir putaran looping, harga 
        seluruh produk akan ter-akumulasi
    - Setelah seluruh proses looping selesai, program akan menampilkan total harga keseluruhan dari produk yang tersimpan di dalam keranjang
    '''
    def hitung(self):
        harga_item = 0
        total_belanja = 0
        for data in self.produk_list:
            harga_item = data.harga
            total_belanja = total_belanja + harga_item
        print ("~"*50)
        print (f"Total belanja = Rp {total_belanja},-")
        print ("~"*50)
        print ("")
        print ("")    

    '''
    Method ini berisi program untuk menghapus produk yang ada di dalam keranjang
    Cara kerja : 
    - Program akan meminta user memasukkan nama produk yang akan di hapus dari keranjang
    - Selanjutnya sistem akan melakukan looping berdasarkan jumlah produk yang ada di dalam keranjang.
    - Pada proses looping, program akan mencocokkan nilai dari variabel "hapus_item" yang sebelumnya di input oleh user, dengan index pertama daftar produk yang berisikan nama produk
    - Apabila nilai dari variabel tidak sama dengan nama produk yang tersimpan, maka akan melakukan putaran looping selanjutnya hingga nilai variabel "hapus_item" sama dengan nama produknya
    - Ketika sudah menemukan index yang sesuai, program akan menghapus index tersebut menggunakan .remove(), dan memberikan notifikasi bahwa produk tersebut berhasil dihapus dari keranjang
    '''
    def hapus(self):
        hapus_item = input("Masukkan produk yang akan di hapus : ")
        hapus_item = hapus_item.capitalize()

        i = 0
        for data in self.produk_list:
            if hapus_item != data.produk:
                i+=1
            else:
                hapus_item == data.produk
                self.produk_list.remove(data)
                print ("~"*50)
                print (f"{data.produk} berhasil dihapus dari keranjang")
                print ("~"*50)
                print ("")
                print ("")
                
#inisialisasi class            
#cart = CartItem('',0)
    '''
    Program utama dari aplikasi ini yang berisikan User interface yang berkaitan langsung dengan pengguna
    Cara kerja : 
    - Program ini menggunakan looping "while" dengan memasukkan nilai awal "Exit=False" sehingga program akan terus berjalan sampai user memilih menu "exit" yang merubah nilai "Exit" menjadi "True"
        dan menghentikan program.
    - Ketika dijalankan, program akan menampilkan menu yang dapat dipilih oleh user, setiap menu akan terhubung dengan method nya masing-masing
    - Variabel "pilih" dibuat sebagai default variabel untuk memilih menu, nilai defaultnya adalah "0" dan akan berubah sesuai dengan nomor menu yang dipilih oleh user.
    - Terdapat validasi pada bagian ini, sehingga apabila user memasukkan nilai yang bukan berupa angka, dan diluar dari pilihan yang tersedia, akan memunculkan notifikasi untuk memilih 
        menu yang benar
    - Untuk setiap pilihan menu yang dipilih, akan menjalankan method yang sesuai dengan yang dipilih.
    - Ketika user memilih menu nomor 5 (exit), maka akan merubah variabel "exit" menjadi "True" dan akan menghentikan program ini.

    ''' 
    def handwitantoApp(self):
        exit = False
        while exit == False:
            print ("")
            print ("MENU UTAMA")
            print ("="*30)
            print ("")

            print ("Menu : ")
            print ("1. Masukkan barang ke keranjang")
            print ("2. Menghapus barang dari keranjang")
            print ("3. Lihat barang di keranjang")
            print ("4. Menghitung total belanja")
            print ("5. Exit")
            print("")

            pilih = 0
            try:
                pilih = int(input("Pilihan : "))
            except:
                print ("masukkan pilihan berupa angka")
            if pilih == 1:
                shop.beli()
            elif pilih == 2:
                shop.hapus()
            elif pilih == 3:
                shop.lihat()
            elif pilih == 4:
                shop.hitung()
            elif pilih == 5:
                exit = True
                print ("")
                print ("")
                print ("="*50)
                print ("Terima kasih, selamat berbelanja kembali!")
                print ("="*50)
                break
            else:
                print("pilih menu angka 1 sampai 5")
        

shop = Shooping([],0,0,'')
shop.handwitantoApp()
#shop.lihat()
