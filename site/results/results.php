<?php
	/*
	 * results.php
	 * 
	 * The results of the searched book. Also calls the Voertman's script file.
	 *
	 * Author: Parker Cantu, Jacob Cole (PHP)
	 *
	 */
	session_start();
	include '../php/getUntData.php';
	unset($_SESSION["deptNumber"]);
	unset($_SESSION["courseNumber"]);
	unset($_SESSION["bookNewVoert"]);
	unset($_SESSION["bookRentalVoert"]);
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
					$deptArray = explode("|", $_POST["department"]);
					$deptNumber = $deptArray[0];
					$deptName = $deptArray[1];
					$_SESSION["deptNumber"] = $deptNumber;
					$_SESSION["courseNumber"] = $_POST["course"]; 
					queryDataUnt($deptName, $_POST["course"]);
					//check only book name. book name should always be present if a book is available.
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
				<span id="loading" hidden>Scraping data...</span>
				<p>
				</p>
			</div>
			<div id="unt" class="bookstore">
				<h1>UNT Bookstore</h1>
				<p>
					<?php if(isset($GLOBALS["priceNewUnt"])) : ?>
						New: $<?=$GLOBALS["priceNewUnt"];?>
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
<?php if(isset($GLOBALS["name"])) : ?>
	<script type="text/javascript" language="JavaScript">
		$("#loading").show();
	    $.ajax({
			type: "POST",
			dataType: "json",
			url: "../python/untextbookfinder/processForm.php",
			success: function(data) {
			
				if (data != null) {
					var bookNew = data["bookNew"] + "<br/>";
					var bookRental = data["bookRental"];
				} else {
					var bookNewVoert = "";
					var bookRentalVoert = "";
				}

				$("#loading").hide();

				//display both, or 1
				if(bookNew != "<br/>" && bookNew != "") {
					$("#voertmans p").append(bookNew.trim());
					$("#voertmans p").append(bookRental.trim());
				} else if (bookNew != "<br/>") {
					$("#voertmans p").append(bookNew.trim());
				} else if (bookRental != "") {
					$("#voertmans p").append(bookRental.trim());
				}
			},
			error: function() {
				$("#loading").hide();
				$("#voertmans p").append("Book prices unavailable.");
			}
	    });
	</script>
<?php endif; ?>