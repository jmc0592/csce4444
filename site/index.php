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
		<form id="bookform" action="python/untextbookfinder/processForm.php" method="post">
			<div id = "select">
				<select class = "selectmenus" name = "department" form="bookform">
					<option value="" disabled="disabled" selected="selected">Select</option>
					<option value="198">ACCT - ACCOUNTING</option>
				</select>
				<select class = "selectmenus" name = "course" form="bookform">
					<option value="" disabled="disabled" selected="selected">Select</option>
					<option value="2010">2010 - ACCOUNTING PRINCIPLES I</option>
					<option value="2020">2020 - ACCOUNTING PRINCIPLES II</option>
					<option value="3110">3110 - INTERMEDIATE ACCOUNTING I</option>
					<option value="3120">3120 - INTERMEDIATE ACCT II</option>
					<option value="3270">3270 - COST ACCOUNTING</option>
					<option value="3405">3405 - PROFESSIONAL DEVELOPMENT</option>
					<option value="4100">4100 - ACCOUNTING SYSTEMS</option>
					<option value="4300">4300 - FEDERAL INCOME TAXATION</option>
					<option value="4400">4400 - AUDITING PROFESSIONAL RESPONSIBILITIES</option>
					<option value="4800">4800 - INTERNSHIPS</option>
					<option value="4900">4900 - INTERNSHIPS</option>
					<option value="5020">5020 - ACCOUNTING DATA</option>
					<option value="5110">5110 - FUNDAMENTALS OF ACCOUNTING RESEARCH</option>
					<option value="5120">5120 - I.S. IN ACCOUNTING</option>
					<option value="5130">5130 - ACCT FOR MGMT</option>
					<option value="5140">5140 - ADVANCED ACCOUNTING ANALYSIS</option>
					<option value="5200">5200 - PRO ETHICS &amp; CORPORATE GOVERNANCE</option>
					<option value="5250">5250 - STRATEGIC COST MANAGEMENT</option>
					<option value="5310">5310 - TAX RSRCH &amp; ADMIN PROC</option>
					<option value="5320">5320 - TAXATION OF CORPORATIONS, PARTNERSHIPS AND FIDUCIARIES</option>
					<option value="5330">5330 - TAXATION OF CORPORATIONS AND SHAREHOLDERS</option>
					<option value="5340">5340 - OIL &amp; GAS TAXATION</option>
					<option value="5360">5360 - ADVANCED TOPICS IN FEDERAL TAXATION</option>
					<option value="5370">5370 - FAM * TAX PLAN</option>
					<option value="5410">5410 - AUDIT INVESTIGATIVE PROCESS</option>
					<option value="5440">5440 - EDP AUDITING</option>
					<option value="5480">5480 - FRAUD EXAMINATION</option>
					<option value="5710">5710 - STUDIES IN SHAKESPEARE</option>
					<option value="5760">5760 - CONTEMPORARY ISSUES IN ACCOUNTING</option>
					<option value="5800">5800 - INTERNSHIP</option>
					<option value="5900">5900 - DIRECTED STUDY</option>
					<option value="6010">6010 - SEMINAR ON ADVANCED TOPICS IN ACCOUNTING RESEARCH</option>
					<option value="6900">6900 - SPECIAL PROBLEMS</option>
					<option value="6910">6910 - SPECIAL PROBLEMS</option>
					<option value="6940">6940 - INDIVIDUAL RESEARCH</option>
					<option value="6950">6950 - DOCTORAL DISSERTATION</option>
				</select>
				<select class = "selectmenus" name = "section" form="bookform">
					<option value="" disabled="disabled" selected="selected">Select</option>
					<option value="41334">ALL</option>
				</select>
			<input id="button" type = "submit">
		</div>
		</form>
	</div>
	<div id = "footer">
	</div>
</body>