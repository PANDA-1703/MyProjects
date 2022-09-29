<?php 

require 'functions.php';
require 'db/db.php';
require __DIR__ . "/vendor/autoload.php";
use DiDom\Document;

$url = 'http://www.arbitat.ru/public/purchases-all/';
$pageNum = '02'; //указать страницу сайта

getURL($url, $pageNum);

$document = new Document('1.html', true); // запись html в файл
$document2 = new Document('2.html', true);

$posts = $document->find('.gridRow');
file_put_contents('2.html', $posts); // запись выбранных данных в файл

$link = mysqli_connect('localhost', 'panda', 'Test123test!', 'panda')
or die("Ошибка " . mysqli_error($link));;

//парсинг и выборка 
$arr_text[] = '';
$num = $document->find('.purchase-type-auction-open, .tip-lot href, .gridAltColumn a, .columnCurrency, .columnDateTime');
//file_put_contents('3.html', $num);
foreach($num as $numb){
    $first = $numb->text();
    $second = $numb->href;
    array_push($arr_text, $first, $second);
}

//запись в бд / вывод в консоль 
for ($i = 5; $i<count($arr_text)-5; $i=($i+8)){
    $auctionNumber = (int)$arr_text[$i];
    $numberLot = (int)$arr_text[$i+2];
    $linkLot = (string)$arr_text[$i+3];
    $crutch = preg_replace("/[\t\r\n]+/",' ',$arr_text[$i+4]);  //удаляет лишние табуляции из строки
    $startPrice = (string)$crutch;
    $dateEvent = (string)$arr_text[$i+6];
    if  ($i==21 or $i==29 or $i==45) //лоты 3-ий, 4-ый и 6-ой сверху
    {
        getTable($link, $auctionNumber, $numberLot, $linkLot, $startPrice, $dateEvent);
        echo " | " . $auctionNumber . " | " . $numberLot . " | " . $linkLot . " | " . $startPrice . " | " . $dateEvent . " | " . "\n";
    }
}

//print_r($arr_text);
//print_r($arr_href);
