
<?php
/*
 * processForm.php
 *
 * Script to run the Voertman's scraper and return the book information if available.
 * NOTE: This needs to be in the python directory to execute the scrapy command.
 *
 * Author: Jacob Cole
 */
    session_start();
    //command to get voertmans book info
    $command = "../../libraries/scrapy crawl voertmans -a departmentChoice=" . 
        $_SESSION["deptNumber"] . " -a courseChoice=" . $_SESSION["courseNumber"] . " -a sectionChoice=41334";
    exec($command, $result);

    if(isset($result[0])){
        unset($_SESSION["deptNumber"]);
        unset($_SESSION["courseNumber"]);

        $resultData = json_decode($result[0], true);

        echo json_encode($resultData);
    }
?>