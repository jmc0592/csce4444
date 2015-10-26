<html>
	<body>
		<h1>Page for testing python calls from php</h1>
		<?php
			$python = 'python ../python/test.py';
			$result = [];
			exec($python, $result);
			echo var_export($result);
		?>
	</body>
</html>