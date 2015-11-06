<!DOCTYPE html>
<head>
	<link rel="stylesheet" type="text/css" href="css\stylesheet.css" />
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
</head>

<body>
	<div id = "banner">
		<div id = "bannertext"><h1>UNTextbookFinder</h1></div>
	</div>
	<div id = "left">
		<p><a href="">Home</a></p>
		<p><a href="">About Us</a></p>
	</div>
	<div id = "right">
		<form id="bookform" action="search/search.php">
			<div id = "select">
				<select class = "selectmenus" name = "department" form="bookform">
					<option value="" disabled="disabled" selected="selected">Select</option>
					<option value="option1">option1</option>
					<option value="option2">option2</option>
					<option value="option3">option3</option>
					<option value="option4">option4</option>
				</select>
				<select class = "selectmenus" name = "course" form="bookform">
					<option value="" disabled="disabled" selected="selected">Select</option>
					<option value="option1">option1</option>
					<option value="option2">option2</option>
					<option value="option3">option3</option>
					<option value="option4">option4</option>
				</select>
				<select class = "selectmenus" name = "section" form="bookform">
					<option value="" disabled="disabled" selected="selected">Select</option>
					<option value="option1">option1</option>
					<option value="option2">option2</option>
					<option value="option3">option3</option>
					<option value="option4">option4</option>
				</select>
			<input id="button" type = "submit">
		</div>
		</form>
	</div>
	<div id = "footer">
	</div>
</body>