<?php
$mahasiswa = [
    ["nim" => "2023001", "nama" => "Andi", "nilai" => 85],
    ["nim" => "2023002", "nama" => "Budi", "nilai" => 72],
    ["nim" => "2023003", "nama" => "Citra", "nilai" => 90],
    ["nim" => "2023004", "nama" => "Dewi", "nilai" => 60],
];

// Hitung jumlah mahasiswa yang lulus menggunakan array_filter
$jumlahLulus = count(array_filter($mahasiswa, fn($m) => $m['nilai'] >= 80));
?>

<h3>Data Mahasiswa</h3>
<table border="1" cellpadding="8" cellspacing="0">
    <tr>
        <th>NIM</th>
        <th>Nama</th>
        <th>Nilai</th>
        <th>Keterangan</th>
    </tr>
    <?php foreach ($mahasiswa as $m): ?>
        <tr>
            <td><?= $m['nim'] ?></td>
            <td><?= $m['nama'] ?></td>
            <td><?= $m['nilai'] ?></td>
            <td><?= $m['nilai'] >= 80 ? 'Lulus' : 'Tidak Lulus' ?></td>
        </tr>
    <?php endforeach; ?>
</table>

<br>
<strong>Jumlah mahasiswa yang lulus: <?= $jumlahLulus ?></strong>