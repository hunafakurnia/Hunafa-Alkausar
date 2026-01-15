<?php
//$arraybuah = ['Mangga','Apel','Pisang','Jeruk'];
$arraybuah[0] = 'Mangga';
$arraybuah[1] = 'Apel';
$arraybuah[2] = 'Pisang';
$arraybuah[3] = 'Jeruk';
$arraybuah[4] = 'Durian';
$arraybuah[5] = 'Nanas';

echo "<select>";

$jmldata = count($arraybuah); // 6
for ($i = 0; $i < $jmldata; $i++) {
    echo "<option>{$arraybuah[$i]}</option>";
}
echo "</select>";

// array asosiatif -> index string
$arrayAvenger = [
[
    "name" => "iron man",
    "age" => 45,
    "color" => "red",
],
[
    "name" => "hulk",
    "age" => 9,
    "color" => "green",
],
[
    "name" => "capten america",
    "age" => 34,
    "color" => "blue",
],
];

foreach($arrayAvenger as $data) {
    echo "name : ".$data['name'];
    echo "age : ".$data['age'];
    echo "color : ".$data['color'];
}
?>
