from flask import Flask, render_template, request, redirect, url_for, flash
from db import fetch_all_items, insert_paket, fetch_item_by_id, update_paket, delete_paket

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    paket_wisata = fetch_all_items()
    return render_template('index.html', paket_wisata=paket_wisata)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        nama_paket = request.form['nama_paket']
        gunung = request.form['gunung']
        harga = request.form['harga']
        fasilitas = request.form['fasilitas']
        insert_paket(nama_paket, gunung, harga, fasilitas)
        flash('Data paket wisata berhasil ditambahkan!', 'success')
        return redirect(url_for('index') + "#about")
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    paket = fetch_item_by_id(id)
    if request.method == 'POST':
        nama_paket = request.form['nama_paket']
        gunung = request.form['gunung']
        harga = request.form['harga']
        fasilitas = request.form['fasilitas']
        update_paket(id, nama_paket, gunung, harga, fasilitas)
        flash('Data paket wisata berhasil diubah!', 'success')
        return redirect(url_for('index') + "#about")
    return render_template('edit.html', paket=paket)

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    delete_paket(id)
    flash('Data paket wisata berhasil dihapus!', 'success')
    return redirect(url_for('index') + "#about")
    
if __name__ == '__main__':
    app.run(debug=True)