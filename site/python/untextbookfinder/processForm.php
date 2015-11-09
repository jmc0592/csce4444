
<?php
/*
 * This needs to be in the python directory to execute the scrapy command. Consider reorganization of project strucutre in future.
 */
        session_start();

        //command to get voertmans book info
        $command = "/Library/Frameworks/Python.framework/Versions/2.7/bin/scrapy crawl voertmans -a departmentChoice=" . 
            $_POST["department"] . " -a courseChoice=" . $_POST["course"] . " -a sectionChoice=" . $_POST["section"];
        exec($command, $result);
        if(isset($result[0])){
            $resultData = json_decode($result[0], true);

            $_SESSION["bookName"] = $resultData["bookName"];
            $_SESSION["bookNew"] = $resultData["bookNew"];
            $_SESSION["bookRental"] = $resultData["bookRental"];
        }

        //goes to search page
        echo '<script type="text/javascript">';
        echo 'window.location.href = "http://localhost/csce4444/site/search/search.php"';
        echo '</script>';
?>