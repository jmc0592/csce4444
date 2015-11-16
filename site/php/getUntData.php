<?php
/*
 * getUnData.php
 *
 * This script queries from our online database at Parse.com
 * 
 * Author: Jacob Cole
 */
require '../parseConnect.php';
use Parse\ParseObject;
use Parse\ParseQuery;
use Parse\ParseException;

function queryDataUnt($department, $course, $section = "001") {

    $query = new ParseQuery("Book");
    $query->startsWith("department", $department);
    $query->equalTo("course", $course);
    //$query->startsWith("section", $section);
    $query->limit(1);

    try {
        $result = $query->find();
        if(isset($result[0])) {
        $object = $result[0];
            $GLOBALS['isbn'] = $object->get("isbn");
            $GLOBALS['name'] = $object->get("name");
            $GLOBALS['priceNewUnt'] = $object->get("priceNew");
        }
    } catch (ParseException $ex) {
        echo "Book not found in database.";
    }
}
?>