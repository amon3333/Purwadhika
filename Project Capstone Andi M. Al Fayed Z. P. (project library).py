
book= [
    {'id':1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925,'stock':4, 'availability':True, 'times_borrowed':101},
    {'id':2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960,'stock':3, 'availability':True,'times_borrowed':34},
    {'id':3, "title": "1984", "author": "George Orwell", "year": 1949, 'stock':6, 'availability':True,'times_borrowed':20},
    {'id':4, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, 'stock':1, 'availability':True, 'times_borrowed':42},
    {'id':5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951,'stock':0, 'availability':False, 'times_borrowed':104},
    {'id':6, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, 'stock':0, 'availability':False, 'times_borrowed':105},
    {'id':7, "title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "year": 1997, 'stock':15, 'availability':True, 'times_borrowed':32},
    {'id':8, "title": "Moby-Dick", "author": "Herman Melville", "year": 1851,'stock':0, 'availability':False, 'times_borrowed':25},
  
]


peminjam = []


def table_length(a, b):
    max_length = max(len(x[a]) for x in book)
    return " "*(max_length - len(b))

def table_length_peminjam(a, b):
    max_length = max(len(x[a]) for x in peminjam)
    return " "*(max_length - len(b))


def availability(list):
    for x in range(len(list)):
        if list[x]['availability']==True and list[x]['stock']!=0:
            list[x]['availability']='tersedia'
        else:
            list[x]['availability']='tidak tersedia'

def reset(list):
    for x in range(len(list)):
        if list[x]['availability']=='tersedia':
            list[x]['availability']=True
        else:
            list[x]['availability']=False


def table_list():
    print ('*'*90)
    availability(book)
    print('index\t|' + 'Judul' + table_length('title', 'Judul') + '|' + 'Penulis' + table_length('author', 'Penulis') + '|' + 'Ketersediaan'+ table_length('availability', 'ketersediaan')+'|')
    for x in range(len(book)):
        print('{}\t|{}{}|{}{}|{}{}|'.format(x+1, book[x]['title'], table_length('title', book[x]['title']), book[x]['author'],table_length('author', book[x]['author']), book[x]['availability'],table_length('availability', book[x]['availability'])))
    reset(book)


def _title (_list):
    if len(_list)==1:
        print (_list[0])
    
    else:
        print ('*'*90)
        print (_list[0])
        print ('*'*90)
        for x in range(1, len(_list)):
            print (_list[x])

def option_frame (table, title_pilihan, pilihan_function, fail):
    table()
    print('*'*90)
    while True:
        try:
            print('*'*90)
            if len(title_pilihan)!=1:
                print('\t\t\t\t' + title_pilihan[0])
                print('*'*90)
                for x in title_pilihan[1:]:
                    print('\t\t\t\t' + x)
                _input = int(input('\t\t\t\tMasukkan pilihan: '))
                if 0<_input < len(pilihan_function):
                    pilihan_function[_input-1]()
                elif _input<=0 or _input>len(pilihan_function):
                    print ('\t\t\t\tmohon maaf input anda melebihi batas')
                    continue
                else:
                    break
            else:
                for x in title_pilihan:
                    print(x)
                    print('*'*90)
                pilihan_function = int(input('\tMasukkan index buku yang ingin dihapus(jika ingin kembali, ketik -1): '))
                if pilihan_function in range(len(book)+1):
                    print('*'*90)
                    for x in range(len(book)):
                        if x+1 == pilihan_function:
                            print (f'\t\tBuku "{book[x]["title"]}" dihapus dari perpustakaan.')
                            for y in range(len(peminjam)):
                                if book[x]['title']==peminjam[y]['title']:
                                    del peminjam[y]
                            del book[x]
                    

                elif pilihan_function < 0:
                    break
                else:
                    print('*'*90)
                    print(f"{pilihan_function} tidak terdapat sebagai index")
                print('*'*90)
                end = str(input('\t\tapakah anda ingin melanjutkan menghapus (ya/tidak): ')).lower()
                end = end.replace(' ','')
                if end == 'tidak':
                    break
            
   
        except ValueError:
                print('*'*90)
                print(fail)

def pinjam_buku():
    input_pinjam = int(input('\t\t\t\tMasukkan index buku yang ingin dipinjam: '))
                        
    if book[input_pinjam-1]['stock']==0:
        print ('\t\t\t\tstock buku {} tidak tersedia'.format(book[input_pinjam-1]['title']))
    else:
        print ('\t\t\t\tBuku yang anda pinjam adalah {}'.format(book[input_pinjam-1]['title'],book[input_pinjam-1]['stock'] ))
        input_nama = str(input('\t\t\t\tMasukkan nama peminjam: '))           
       
        for x in range(len(book)):
            if x+1 == input_pinjam:
                book[x]['stock']=book[x]['stock']-1
                book[x]['times_borrowed']+=1
                
        pinjaman = {'id':len(peminjam)+1, 'title':book[input_pinjam-1]['title'], 'nama':input_nama}
        peminjam.append(pinjaman)
        print('*'*90)
        print('\t\tbuku {} dipinjam oleh {} dengan id pengembalian {}'.format(book[input_pinjam-1]['title'], input_nama, peminjam[len(peminjam)-1]['id']))
        

def ranked():
    ranked_books = sorted(book, key=lambda x: x['times_borrowed'], reverse=True)
    top_books = ranked_books[:3]
    print('*'*90)
    print('\t\tini adalah ketiga buku yang paling sering dipinjam')
    for x, y in enumerate(top_books, start=1):
        print(f'\t\trank {x}, {y["title"]} dengan kali dipinjam sebanyak {y["times_borrowed"]}')

def exit_menu():
    return 

def pengembalian_buku():
    try:
        input_id = int(input('\t\t\t\tMasukkan id peminjam: '))
        if input_id-1 in range(len(peminjam)):
            print('*'*90)
            for x in range(len(peminjam)):
                if input_id == peminjam[x]['id']:
                    print ('\t\t\tbuku {} berhasil dikembalikan'.format(peminjam[x]['title']))
                    for y in range(len(book)):
                        if book[y]['title']==peminjam[x]['title']:
                            book[y]['stock'] = book[y]['stock']+1
                    del peminjam[x]          
        else:
            print('*'*90)
            print('\t\t\t\tid peminjam tidak ditemukan')
    except:
        print('*'*90)
        print('\t\t\tinput yang dimasukkan salah. Mohon menggunakan angka.')
    


def update_buku(title_opsi=['Masukkan aspek buku yang ingin diubah', '1. Judul','2. Penulis','3. Tahun', '4. Ketersediaan'] ):
    while True:
        try:
            table_list()
            print('*'*90)
            input1=int(input('\t\t\tMasukkan index buku yang ingin diupdate: '))
            print('*'*90)
            availability(book)
            print ('\t\t\tbuku yang ingin di update adalah\n','|{}{}|{}{}|{}|{}|{}{}|'.format('Judul', table_length('title', 'Judul'), 'Penulis',table_length('author', 'Penulis') ,'Tahun','Stock','Ketersediaan',table_length('availability', 'Ketersediaan')))
            print (' |{}{}|{}{}| {}|    {}|{}{}|'.format(book[input1-1]['title'],table_length('title', book[input1-1]['title']), book[input1-1]['author'],table_length('author', book[input1-1]['author']),book[input1-1]['year'], book[input1-1]['stock'],book[input1-1]['availability'],table_length('availability', book[input1-1]['availability'])))
            reset(book)
            print('*'*90)
            print('\t\t\t\t' + title_opsi[0])
            for x in title_opsi[1:]:
                print('\t\t\t\t' + x)                
            input2 = int(input('\t\t\tMasukkan aspek yang ingin di ubah: '))
            if input2 == 1:
                print ('\t\t\tbuku {}'.format(book[input1-1]['title']))
                input3 = str(input('\t\t\tMasukkan nama buku baru: '))
                book[input1-1]['title']=input3
                print('*'*90)
                print ('\t\t\tnama buku berhasil diubah menjadi {}'.format(book[input1-1]['title']))
                break
            elif input2 == 2:
                print ('\t\t\tbuku {} ditulis oleh {}'.format(book[input1-1]['title'],book[input1-1]['author']))
                input3 = str(input('\t\t\tMasukkan nama penulis baru: '))
                book[input1-1]['author']=input3
                print('*'*90)
                print ('\t\t\tnama penulis buku berhasil diubah menjadi {}'.format(book[input1-1]['author']))
                break
            elif input2 == 3:
                print ('buku {} diterbitkan di tahun{}'.format(book[input1-1]['title'], book[input1-1]['year']))
                input3 = int(input('\t\t\tMasukkan tahun baru: '))
                book[input1-1]['year']=input3
                print('*'*90)
                print ('\t\t\tTahun berhasil diubah menjadi {}'.format(book[input1-1]['year']))
                break
            elif input2 == 4:
                availability(book)
                
                print ('\t\t\tbuku {} {} di perpustakaan ini'.format(book[input1-1]['title'], book[input1-1]['availability']))
                input3 = int(input('\t\t\tUpdate stock buku (masukkan angka): '))

                if input3 > 0:
                    book[input1-1]['availability'] = 'tersedia'
                    book[input1-1]['stock']= input3
                    print('*'*90)
                    print('\t\t\tbuku {} {} dengan stock {}'.format(book[input1-1]['title'], book[input1-1]['availability'], book[input1-1]['stock']))
                    reset(book)
                    break
                else :
                    book[input1-1]['availability']= 'tidak tersedia'
                    book[input1-1]['stock']= 0
                    print('*'*90)
                    print('\t\t\tbuku {} {}'.format(book[input1-1]['title'], book[input1-1]['availability']))
                    reset(book)
                    break
            else:
                break

        except ValueError:
            print('\t\t\tInput salah. Mohon masukkan angka')

def menambah_buku():
    
    judul = str(input("\t\t\t\tMasukkan nama buku: "))
    penulis = str(input('\t\t\t\tMasukkan nama penulis: '))
    tahun = int(input('\t\t\t\tMasukkan tahun terbit: '))
    stock = int(input('\t\t\t\tMasukkan jumlah buku: '))
    
    new_book = {'id':len(book)+1, "title": judul, "author": penulis, "year": tahun, 'stock':stock, 'availability': True, 'times_borrowed':0}
    book.append(new_book)
    print ('*'*90)
    print(f'\t\t\tBuku "{judul}" ditambahkan di perpustakaan.')

def melihat_status():
    try:
        print('*'*90)
        print('\t\tindex\t|' + 'Judul' + table_length_peminjam('title', 'Judul') + '|'  + 'Peminjam'+ table_length_peminjam('nama', 'peminjam')+'|')
        for x in range(len(peminjam)):
            print('\t\t{}\t|{}{}|{}{}|'.format(x+1, peminjam[x]['title'], table_length_peminjam('title', peminjam[x]['title']), peminjam[x]['nama'],table_length_peminjam('nama', peminjam[x]['nama'])))
    except:
        print ('\t\t\t    Tidak ada buku yang dipinjam.')

while True:
    try:
        _title(['\t\t\t   Selamat datang di perpustakaan','\t\t\t\t1. Menu peminjaman buku','\t\t\t\t2. Menu perpustakaan', '\t\t\t\t3. Menghapus buku','\t\t\t\t4. Exit program'])

        nomor = int(input("\t\t\t\tMasukkan angka menu: "))

        if nomor == 1:
            option_frame(table_list, ['Menu Peminjaman','1. Melihat daftar buku','2. Meminjam buku','3. Melihat popularitas buku','4. Mengembalikan buku','5. Kembali ke menu utama'],[table_list, pinjam_buku, ranked, pengembalian_buku , exit_menu],'\t\t\t\tInput yang dimasukkan salah.')
        
        elif nomor == 2:
            option_frame(table_list, ['Menu perpustakaan','1. Mengubah data buku','2. Menambah buku','3. Melihat status peminjaman','4. Kembali ke menu awal'], [update_buku, menambah_buku, melihat_status, exit_menu], '\t\t\tInput invalid. Mohon masukkan angka.')
            
        elif nomor == 3:
            _input=0
            option_frame(table_list,['\t\t\t\tMenu penghapusan buku'], _input , 'Input salah. Hanya menerima angka.')
            
        elif nomor == 4:
            break
        elif nomor<= 0 or nomor>4:
            print('\t\t\t\tmohon maaf, input melebihi batas.')

    except ValueError:
        print('\t\t\t\tmohon maaf, hanya menerima input angka.')
    except:
        print('\t\t\t\tmohon maaf, input melebihi batas.')
        

print('\t\t\tTerima kasih sudah mengunjungi perpustakaan!')