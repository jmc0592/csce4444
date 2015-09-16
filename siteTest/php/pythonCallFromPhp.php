<html>
	<body>
		<h1>Page for testing python calls from php</h1>
		<?php
			$python = 'python /Applications/XAMPP/xamppfiles/htdocs/csce4444/siteTest/python/test.py';
			$result = [];
			exec($python, $result);
			echo var_export($result);
		?>
	</body>
</html>