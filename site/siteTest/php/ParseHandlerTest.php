<?php
    use Parse\ParseObject;

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

            $response = $query->count();
            $this->assertTrue($response == 1);
            
        }
    }
?>