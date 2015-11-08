
<?php
/*
 * This needs to be in the python directory to execute the scrapy command. Consider reorganization of project strucutre in future.
 */
    $command = "/Library/Frameworks/Python.framework/Versions/2.7/bin/scrapy crawl voertmans -a departmentChoice=" . $_POST["department"] . " -a courseChoice=" . 
        $_POST["course"] . " -a sectionChoice=" . $_POST["section"];
    //$command = "/Library/Frameworks/Python.framework/Versions/2.7/bin/scrapy version";
    exec($command, $output, $result);
    echo $result;
    var_dump($output);

    echo "---post test----";
        print_r($_POST["bookName"] . "\n");
    print_r($_POST["bookRental"] . "\n");
    print_r($_POST["bookNew"] . "\n");
?>
<script type="text/javascript">
    window.location.href = 'http://localhost/csce4444/site/search/search.php';
</script>