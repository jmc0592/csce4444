<?php
require '../../parseConnect.php';

use Parse\ParseObject;

$testObject = ParseObject::create("TestObject2");
$testObject->set("foo", "bar");

try {
	$testObject->save();
 	echo 'New object created with objectId: ' . $testObject->getObjectId();
} catch (ParseException $ex) {  
  	// Execute any logic that should take place if the save fails.
  	// error is a ParseException object with an error code and message.
  	echo 'Failed to create new object, with error message: ' . $ex->getMessage();
}
?>