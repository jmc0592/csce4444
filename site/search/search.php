<?php
    echo "---post test----";
    if(isset($_POST)){
        print_r($_POST["bookName"] . "\n");
	    print_r($_POST["bookRental"] . "\n");
	    print_r("new book = " . $_POST["bookNew"] . "\n");
	}
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
		<p><a href="../index.php">Home</a></p>
		<p><a href="">About Us</a></p>
	</div>
	<div id = "right">
		<div id="bookinfo">
			<div id="generalinfo" class="bookstore">
				<h1>Info</h1>
			</div>
			<div id="infodivide"></div>
			<div id="voertmans" class="bookstore">
				<h1>Voertman's</h1>
			</div>
			<div id="unt" class="bookstore">
				<h1>UNT Bookstore</h1>
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