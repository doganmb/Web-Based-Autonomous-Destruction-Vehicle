<?php

$dosya = "json/command.json";
$request = file_get_contents("php://input");
$myFiles = fopen($dosya,"w");

fwrite($myFiles,$request);
fclose($myFiles);


?>