import pymysql

def connect():
    return pymysql.connect(host="localhost", 
                            user="root", 
                            passwd="", 
                            database="Gunung", 
                            cursorclass=pymysql.cursors.DictCursor)

def fetch_all_items():
    connection=connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM paket_wisata"
            cursor.execute(sql)
            rows = cursor.fetchall()
        return rows
    finally:
        connection.close()

def insert_paket(nama_paket, gunung, harga, fasilitas):
    """Menambahkan data paket wisata ke database dengan validasi input."""
    # Validasi input
    if not nama_paket or not gunung or not harga or not fasilitas:
        print("Semua kolom harus diisi! Pastikan nama_paket, gunung, harga, dan fasilitas tidak kosong.")
        return

    # Melanjutkan jika input valid
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO paket_wisata (nama_paket, gunung, harga, fasilitas) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (nama_paket, gunung, harga, fasilitas))
            connection.commit()
            print("Paket berhasil ditambahkan ke database!")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        connection.close()

def fetch_item_by_id(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM paket_wisata WHERE id=%s"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
        return row
    finally:
        connection.close()

def update_paket(id, nama_paket, gunung, harga, fasilitas):
    """
    Mengedit data paket wisata berdasarkan ID.
    """
    # Validasi input
    if not all([id , nama_paket, gunung, harga, fasilitas]):
        print("Error: Semua kolom harus diisi! Pastikan id, nama_paket, gunung, harga, dan fasilitas tidak kosong.")
        return False  # Indikasi bahwa data tidak valid

    # Melanjutkan jika input valid
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE paket_wisata 
            SET nama_paket = %s, gunung = %s, harga = %s, fasilitas = %s 
            WHERE id = %s
            """
            cursor.execute(sql, (nama_paket, gunung, harga, fasilitas, id))
            connection.commit()

            # Mengecek apakah ada baris yang diperbarui
            if cursor.rowcount > 0:
                print("Paket berhasil diperbarui!")
                return True  # Indikasi sukses
            else:
                print("ID paket tidak ditemukan. Tidak ada perubahan.")
                return False  # Indikasi gagal karena ID tidak ditemukan
    except Exception as e:
        print("Terjadi kesalahan:", e)
        return False  # Indikasi gagal karena kesalahan
    finally:
        connection.close()

def delete_paket(id):
    """
    Menghapus data paket wisata berdasarkan ID.
    """
    # Validasi input
    if not id:
        print("Error: ID paket harus diisi untuk menghapus data.")
        return False  # Indikasi bahwa input tidak valid

    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM paket_wisata WHERE id = %s"
            cursor.execute(sql, (id,))
            connection.commit()

            # Mengecek apakah ada baris yang dihapus
            if cursor.rowcount > 0:
                print("Paket berhasil dihapus!")
                return True  # Indikasi sukses
            else:
                print("ID paket tidak ditemukan. Tidak ada data yang dihapus.")
                return False  # Indikasi gagal karena ID tidak ditemukan
    except Exception as e:
        print("Terjadi kesalahan:", e)
        return False  # Indikasi gagal karena kesalahan
    finally:
        connection.close()



    