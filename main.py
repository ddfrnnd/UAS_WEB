from flask import Flask, render_template, request, redirect, url_for, flash, session
from db import fetch_all_items, insert_paket, fetch_item_by_id, update_paket, delete_paket

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    paket_wisata = fetch_all_items() ## untuk mendapatkan semua data dari database disimpan dalam variabel paket_wisata
    return render_template('index.html', paket_wisata=paket_wisata) ## mengirimkan data paket_wisata ke dalam template HTML

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST': ## Mengecek apakah metode HTTP yang diterima adalah POST. Jika iya, maka data yang dikirim melalui formulir akan diproses.
        nama_paket = request.form['nama_paket'] ## Mengakses data yang dikirimkan melalui formulir HTML dengan metode POST.
        gunung = request.form['gunung']
        harga = request.form['harga']
        fasilitas = request.form['fasilitas']
        insert_paket(nama_paket, gunung, harga, fasilitas) ##  menyimpan data ke dalam database
        flash('Data paket wisata berhasil ditambahkan!', 'success')
        session['message'] = 'Data paket wisata berhasil ditambahkan!'
        session['category'] = 'success'
        return redirect(url_for('index') + "#about")
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['POST', 'GET']) ## Mendefinisikan rute edit dengan parameter id
def edit(id):
    paket = fetch_item_by_id(id) ## Mengambil data paket wisata berdasarkan id
    if request.method == 'POST':
        nama_paket = request.form['nama_paket']
        gunung = request.form['gunung']
        harga = request.form['harga']
        fasilitas = request.form['fasilitas']
        update_paket(id, nama_paket, gunung, harga, fasilitas)
        flash('Data paket wisata berhasil diedit!', 'success')
        session['message'] = 'Data paket wisata berhasil diedit!'
        session['category'] = 'success'
        return redirect(url_for('index') + "#about")
    return render_template('edit.html', paket=paket)

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    delete_paket(id)
    flash('Data paket wisata berhasil dihapus!', 'success')
    session['message'] = 'Data paket wisata berhasil dihapus!'
    session['category'] = 'success'
    return redirect(url_for('index') + "#about")
    
if __name__ == '__main__':
    app.run(debug=True)