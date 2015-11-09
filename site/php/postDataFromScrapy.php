<?php
    session_start();
    print_r($_POST["bookName"] . "\n");
    print_r($_POST["bookRental"] . "\n");
    print_r($_POST["bookNew"] . "\n");

    $_SESSION["bookName"] = $_POST["bookName"];
    $_SESSION["bookRental"] = $_POST["bookRental"];
    $_SESSION["bookNew"] = $_POST["bookNew"];
?>