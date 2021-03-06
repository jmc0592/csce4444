<?php
    /*
     * ParseHandlerTest.php
     *
     * Unit test for the Parse file
     *
     * Author: Jacob Cole
     */
    require '../parseConnect.php';
    use Parse\ParseObject;
    use Parse\ParseQuery;

    class ParseHandlerTest extends PHPUnit_Framework_TestCase
    {
        public function testQueryDataUnt() {
            $department = "ACCT";
            $course = "2010";
            $section ="001";

            $obj = ParseObject::create('TestObject');
            $obj->set('department', $department);
            $obj->set('course', $course);
            $obj->set('section', $section);
            $obj->save();

            $query = new ParseQuery('TestObject');
            $query->startsWith('department', $department);
            $query->equalTo('course', $course);
            $query->startsWith('section', $section);
            $query->limit(1);

            $response = $query->find();
            $this->assertTrue(count($response) == 1);  
        }
    }
?>