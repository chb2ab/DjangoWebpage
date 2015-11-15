<?php
### Init session to count correctness ###
session_start();

### Connect to mysql ###
$servername = "localhost";
$username = "new";
$password = "pw";
$dbname = "a3db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error):
    die("Connection failed: " . $conn->connect_error);
endif;


$seed = (int)(date('Y') . date('m') . date('d'));
if ( isset($_POST["getoverall"]) ):
	### Respond to query for get overall results ###
	$query = "SELECT incorrect, correct FROM results WHERE date ='$seed'";
	$result = $conn->query($query);
	$row = $result->fetch_array();
	$ret = array();
	$ret[] = $row["correct"];
	$ret[] = $row["incorrect"];
	echo( json_encode($ret) );
else:
	if( isset($_POST["correct"]) ):
		### Respond to query for correctedness ###
		$_SESSION["correct"] += 1;
		$query = "UPDATE results SET correct = correct + 1 WHERE date = $seed";
		$conn->query($query);
	else:
		$_SESSION["incorrect"] += 1;
		$query = "UPDATE results SET incorrect = incorrect + 1 WHERE date = $seed";
		$conn->query($query);
	endif;
endif;
?>
