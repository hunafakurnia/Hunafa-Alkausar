<?php

// tanggal
$tgl = 1;
echo "<select>";
while ($tgl <= 31) {
    echo "<option>$tgl</option>";
    $tgl++;
}
echo "</select>";

// bulan
$bln = 1;
do {
    echo "<option>$bln</option>";
    $bln++;
} while ($bln <= 12);
echo "</select>";

// tahun
$thn = 2000;
echo "<select>";
while ($thn <= 2030) {
    echo "<option>$thn</option>";
    $thn++;
}
echo "</select>";

?>