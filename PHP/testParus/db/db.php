<?php



function getTableAll($link, $auctionNumber, $numberLot, $linkLot, $startPrice, $dateEvent){

    if(mysqli_connect_errno())
    {
        echo 'Database connection error ('.mysqli_connect_errno().'):' . mysqli_connect_error();
        exit();
    }

    $query = "SELECT linkLot FROM parus";
    $result = mysqli_query($link, $query); //значение в колонке linkLot
    $num_rows = mysqli_num_rows($result); //кол-во строк в бд
    $str[] = '';
    if ($num_rows > 2){ //пуста ли бд (для первого заполнения бд)
        /* извлечение ассоциативного массива */
        while ($row = mysqli_fetch_assoc($result)) {
            array_push($str, implode($row)); 
        }

        if ($linkLot != $str[1] and $linkLot != $str[2] and $linkLot != $str[3]) //проверка одинаковых значений бд
            {
                $sql = "INSERT INTO parus (auctionNumber, numberLot, linkLot, startPrice, dateEvent) VALUES ($auctionNumber, $numberLot, '$linkLot', '$startPrice', '$dateEvent')";
                if (mysqli_query($link, $sql)) {
                    echo "Done";
                } else {
                    echo "Error: " . $sql . "<br>" . mysqli_error($link);
                }
            }
    }
    else {
        $sql = "INSERT INTO parus (auctionNumber, numberLot, linkLot, startPrice, dateEvent) VALUES ($auctionNumber, $numberLot, '$linkLot', '$startPrice', '$dateEvent')";
                if (mysqli_query($link, $sql)) {
                    echo "Done";
                } else {
                    echo "Error: " . $sql . "<br>" . mysqli_error($link);
                }
    }
    

    

}
