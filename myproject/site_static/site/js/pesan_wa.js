function beli() {
    var product_titles = document.getElementsByName('product_title');
    var total_price = document.getElementsByName('total_price')[0].value;
    var nama = document.getElementsByName('nama')[0].value;
    var nomor_hp = document.getElementsByName('nomor_hp')[0].value;
    var pesan = document.getElementsByName('pesan')[0].value;
    var metode_bayar_value = metode_bayar.options[metode_bayar.selectedIndex].value;
    var nama_rekening = document.getElementsByName('nama_rekening')[0].value;
    var id_akun = document.getElementsByName('id_akun')[0].value;

    var products = [];

    for (var i=0; i < product_titles.length; i++) {
        products.push(product_titles[i].value);
    };

    if (nama == "") {
        alert("Nama is required!");
        return false;
    }

    if (nomor_hp == "") {
        alert("Nomor hp is required!");
        return false;
    }

    if (nama_rekening == "") {
        alert("Nama rekening is required!");
        return false;
    }

    if (id_akun == "") {
        alert("Id akun is required!");
        return false;
    }

    var url = "https://api.whatsapp.com/send?phone=6289608372301&text="
        + "FORMAT BELI" + "%0a"
        + "%0a"
        + "Name: " + nama + "%0a"
        + "Nomor hp: " + nomor_hp + "%0a"
        + "Catatan: " + pesan  + "%0a"
        + "Produk: " + products  + "%0a"
        + "Jumlah biaya: Rp " + total_price  + "%0a"
        + "Pembayaran: " + metode_bayar_value  + "%0a"
        + "Nama di rekening/dompet digital: " + nama_rekening  + "%0a"
        + "Id akun: " + id_akun  + "%0a"
        + "%0a"
        + "Keterangan:" + "%0a"
        + "Pastikan nama rekening/dompet digital tujuan pembayaran atas nama Punjung Wirohastomo, "
        + "jika tidak itu merupakan penipuan."

    window.open(url, '_blank').focus();

}