<?php
### Init session to count correctness ###
session_start();
$_SESSION["correct"] = 0;
$_SESSION["incorrect"] = 0;

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

### Generate row in overall results if it doesn't exist ### 
$seed = (int)(date('Y') . date('m') . date('d'));

$query = "SELECT EXISTS(SELECT * FROM results WHERE date ='$seed')";
$result = $conn->query($query);
$row = $result->fetch_array();
$queriedln = (int)$row[0];
if ( $queriedln == 0 ):
	$query = "INSERT INTO results (date, correct, incorrect) VALUES ($seed, 0, 0)";
	$conn->query($query);
endif;

### Generate random quiz ###
srand($seed);
$quizL = rand(0,3); // number of quizzes
$query = "SELECT title FROM quizzes WHERE id ='$quizL'";
$result = $conn->query($query);
$res = $result->fetch_array();
$title = $res["title"];

$quiz = array();
$answers = array();


$query = "SELECT * FROM questions WHERE title ='$title'";
$questions = $conn->query($query);
while($row = $questions->fetch_assoc()):
	$q = array($row["statement"]);
	$cur = $row["id"];
	$query = "SELECT answer, correct FROM answers WHERE questionid ='$cur' and title = '$title' order by RAND()";
	$result = $conn->query($query);
	$it = 0;
	while( $row = $result->fetch_assoc() ):
		$q[] = $row["answer"];
		if ($row["correct"] == 1):
			$answers[] = $it;
		endif;
		$it++;
	endwhile;
	$quiz[] = $q;
endwhile;
$quiz[] = $answers;
$quiz[] = $title;
echo( json_encode($quiz) );
?>
