
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
    $command = "/Library/Frameworks/Python.framework/Versions/2.7/bin/scrapy crawl voertmans -a departmentChoice=" . 
        $_SESSION["deptNumber"] . " -a courseChoice=" . $_SESSION["courseNumber"] . " -a sectionChoice=41334";
    exec($command, $result);

    if(isset($result[0])){
        $resultData = json_decode($result[0], true);

        $_SESSION["bookNewVoert"] = $resultData["bookNew"];
        $_SESSION["bookRentalVoert"] = $resultData["bookRental"];
    }
?>