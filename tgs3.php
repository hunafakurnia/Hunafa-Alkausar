<!DOCTYPE html>
<html>
<body>

<h3>Hotel Sehat</h3>

<form method="post">
    <input type="radio" name="kamar" value="biasa" checked> Biasa (150000 / hari)<br>
    <input type="radio" name="kamar" value="vip"> VIP (200000 / hari)<br>
    <input type="radio" name="kamar" value="super"> Super VIP (400000 / hari)<br><br>

    Lama Inap :
    <input type="number" name="hari" min="1" required><br><br>

    <input type="submit" name="proses" value="Hitung">
</form>

<?php
if (isset($_POST['proses'])) {

    $kamar = $_POST['kamar'];
    $hari  = $_POST['hari'];

    if ($kamar == "biasa") {
        $harga = 150000;
        $nama  = "Biasa";
    } elseif ($kamar == "vip") {
        $harga = 200000;
        $nama  = "VIP";
    } else {
        $harga = 400000;
        $nama  = "Super VIP";
    }

    $total = $harga * $hari;

    if ($hari > 5) {
        $diskon = $total * 0.1;
    } else {
        $diskon = 0;
    }

    $bayar = $total - $diskon;

    echo "<hr>";
    echo "Jenis Kamar : $nama <br>";
    echo "Harga per Hari : Rp $harga <br>";
    echo "Lama Inap : $hari hari <br>";
    echo "Total Harga : Rp $total <br>";
    echo "Diskon 10% : Rp $diskon <br>";
    echo "Total Bayar : Rp $bayar <br>";
}
?>

</body>
</html>
