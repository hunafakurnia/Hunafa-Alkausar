<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Reservasi Hotel Sehat</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
        }
        .container {
            width: 500px;
            margin: 50px auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
        }
        label {
            display: block;
            margin-top: 10px;
        }
        select, input, button {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
        }
        button {
            background: #28a745;
            color: white;
            border: none;
            margin-top: 15px;
            cursor: pointer;
        }
        button:hover {
            background: #218838;
        }
        .hasil {
            margin-top: 20px;
            background: #e9ecef;
            padding: 15px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Reservasi Hotel Sehat</h2>

    <form method="post">
        <label>Jenis Kamar</label>
        <select name="kamar" required>
            <option value="">-- Pilih Kamar --</option>
            <option value="Biasa">Biasa</option>
            <option value="VIP">VIP</option>
            <option value="Super VIP">Super VIP</option>
        </select>

        <label>Lama Inap (hari)</label>
        <input type="number" name="hari" min="1" required>

        <button type="submit" name="hitung">Hitung Total</button>
    </form>

    <?php
    if (isset($_POST['hitung'])) {
        $kamar = $_POST['kamar'];
        $hari  = $_POST['hari'];

        // Harga kamar
        if ($kamar == "Biasa") {
            $harga = 150000;
        } elseif ($kamar == "VIP") {
            $harga = 200000;
        } else {
            $harga = 400000;
        }

        $total = $harga * $hari;
        $diskon = 0;

        // Diskon 10% jika lebih dari 5 hari
        if ($hari > 5) {
            $diskon = 0.1 * $total;
        }

        $bayar = $total - $diskon;
        ?>

        <div class="hasil">
            <p><strong>Jenis Kamar:</strong> <?= $kamar ?></p>
            <p><strong>Harga per Hari:</strong> Rp <?= number_format($harga,0,',','.') ?></p>
            <p><strong>Lama Inap:</strong> <?= $hari ?> hari</p>
            <p><strong>Total Harga:</strong> Rp <?= number_format($total,0,',','.') ?></p>
            <p><strong>Diskon:</strong> Rp <?= number_format($diskon,0,',','.') ?></p>
            <p><strong>Total Bayar:</strong> Rp <?= number_format($bayar,0,',','.') ?></p>
        </div>

    <?php } ?>
</div>

</body>
</html>
