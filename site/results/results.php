<?php
	session_start();
	include '../php/getUntData.php';
?>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="../css/stylesheet.css" />
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
</head>

<body>
	<div id = "banner">
		<div id = "bannertext"><h1>UNTextbookFinder</h1></div>
	</div>
	<div id = "left">
		<p><a href="../index.html">Home</a></p>
		<p><a href="../aboutus/aboutus.html">About Us</a></p>
	</div>
	<div id = "right">
		<div id="bookinfo">
			<div id="generalinfo" class="bookstore">
				<h1>Info</h1>
				<p>
					<?php
					//check only book name. book name should always be present if a book is available.
					$deptArray = explode("|", $_POST["department"]);
					$deptNumber = $deptArray[0];
					$deptName = $deptArray[1];
					queryDataUnt($deptName, $_POST["course"]);
					if(isset($GLOBALS["name"])){
						if(isset($GLOBALS["name"]))
							echo "Name: " . $GLOBALS["name"];
							echo "<br/>";
						if(isset($GLOBALS["isbn"]))
							echo "ISBN: " . $GLOBALS["isbn"];
							echo "<br/>";
					} else {
						echo "Book not available.";
					}
					?>
				</p>
			</div>
			<div id="infodivide"></div>
			<div id="voertmans" class="bookstore">
				<h1>Voertman's</h1>
			</div>
			<div id="unt" class="bookstore">
				<h1>UNT Bookstore</h1>
				<p>
					<?php if(isset($GLOBALS["priceNewUnt"])) : ?>
						New Price - $<?=$GLOBALS["priceNewUnt"];?>
					<?php endif;?>
				</p>
			</div>
			<div id="chegg" class="bookstore">
				<h1>Chegg</h1>
			</div>
			<div id="amazon" class="bookstore">
				<h1>Amazon</h1>
			</div>
		</div>
	</div>
	<div id = "footer">
	</div>
</body>
</html>
<?php
	session_destroy();
?>