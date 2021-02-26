<?php
	$a = $_GET['param1'];
	$b = $_GET['param2'];
	$response = [];
	if (empty($a) or empty($b))
		$response["error"] = true;
	else{
		$response["error"] = false;
		if($a == $b)
			$response["result"] = true;
		else
			$response["result"] = false;
	}
	echo json_encode($response);
?>