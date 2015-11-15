<?php
	$seed = (int)(date('Y') . date('m') . date('d'));
	if ( isset($_COOKIE["time"]) and ($_COOKIE["time"] == $seed) ):
		unset($_COOKIE["time"]);
		setcookie("time", "", time()-3600);
		echo("<center><h1>You've already taken today's quiz</h1></center>");
		echo("<center><h2>Come back tomorrow</h2></center>");
		echo("<br />");
		exit();
	else:
		setcookie("time", $seed);
	endif;
?>
<html>
	<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type = "text/javascript">
var questions;
var answers;

/***
< AJAX REQUEST >
***/
var httpRequest;
if (window.XMLHttpRequest)
{ // Mozilla, Safari, ...
	httpRequest = new XMLHttpRequest();
	if (httpRequest.overrideMimeType)
	{
		httpRequest.overrideMimeType('text/xml');
		// See note below about this line
	}
} 
else if (window.ActiveXObject)
{ // IE
	try
	{
		httpRequest = new ActiveXObject("Msxml2.XMLHTTP");
	} 
	catch (e)
	{
		try
		{
			httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
		} 
		catch (e) {}
	}
}

if (!httpRequest) {
	alert('Giving up :( Cannot create an XMLHTTP instance');
}
httpRequest.onreadystatechange = function()
{ 
	if (httpRequest.readyState == 4) {
			if (httpRequest.status == 200) {
				// Set quiz question and store the rest of questions in variables
				questions = $.parseJSON(httpRequest.responseText);
				document.getElementById("title").innerHTML = "<h3>".concat(questions[questions.length-1], "</h3>");
				document.getElementById("question").innerHTML = "<b>Question ".concat(1, ": </b>", questions[0][0]);
				document.getElementById("Astate").innerHTML = questions[0][1];
				document.getElementById("Bstate").innerHTML = questions[0][2];
				document.getElementById("Cstate").innerHTML = questions[0][3];
				document.getElementById("Dstate").innerHTML = questions[0][4];
				answers = questions[questions.length-2];
			} else {
				alert('There was a problem with the request.');
			}
		}
};
httpRequest.open('POST', "getquiz.php", true);
httpRequest.send(null);
/***
</ Ajax Request >
***/

var qiter = 0;
var correct = 0;
function finish()
{
	/***
	< AJAX REQUEST >
	***/
	var httpRequest2;
	if (window.XMLHttpRequest)
	{ // Mozilla, Safari, ...
		httpRequest2 = new XMLHttpRequest();
		if (httpRequest2.overrideMimeType)
		{
			httpRequest2.overrideMimeType('text/xml');
			// See note below about this line
		}
	} 
	else if (window.ActiveXObject)
	{ // IE
		try
		{
			httpRequest2 = new ActiveXObject("Msxml2.XMLHTTP");
		} 
		catch (e)
		{
			try
			{
				httpRequest2 = new ActiveXObject("Microsoft.XMLHTTP");
			} 
			catch (e) {}
		}
	}

	if (!httpRequest2) {
		alert('Giving up :( Cannot create an XMLHTTP instance');
	}
	httpRequest2.onreadystatechange = function()
	{ 
		if (httpRequest2.readyState == 4) {
				if (httpRequest2.status == 200) {
					// Display overall results to user
					var res = $.parseJSON(httpRequest2.responseText);
					document.getElementById("overall").innerHTML = "Overall results are ".concat(res[0], "/", parseInt(res[0])+parseInt(res[1]), " correct.");
				} else {
					alert('There was a problem with the overall request.');
				}
			}
	};
	httpRequest2.open('POST', "result.php", true);
	var data = new FormData();
	data.append('getoverall', '1');
	httpRequest2.send(data);
	/***
	</ Ajax Request >
	***/

	// Remove question and display overall results
	document.getElementById("question").innerHTML = "Results";
	var parent = document.getElementById("div1");
	var child = document.getElementById("a");
	parent.removeChild(child);
	var child = document.getElementById("Astate");
	parent.removeChild(child);
	var child = document.getElementById("b");
	parent.removeChild(child);
	var child = document.getElementById("Bstate");
	parent.removeChild(child);
	var child = document.getElementById("c");
	parent.removeChild(child);
	var child = document.getElementById("Cstate");
	parent.removeChild(child);
	var child = document.getElementById("d");
	parent.removeChild(child);
	var child = document.getElementById("Dstate");
	parent.removeChild(child);
	var child = document.getElementById("sub");
	parent.removeChild(child);
	document.getElementById("finish").innerHTML = "You got ".concat(correct, "/", questions.length-2, " correct.");
	
}

function next()
{
	// Score current response
	var data = new FormData();
	var chx = document.getElementsByTagName('input');
	for (var i=0; i<chx.length; i++) {
		if (chx[i].type == 'radio' && chx[i].checked) {
			if (i == answers[qiter]) {
				alert("Correct!");
				data.append('correct', '1');
				correct++;
			}
			else {
				alert("Incorrect");
				data.append('incorrect', '1');
			}
			chx[i].checked = false;
		} 
	}

	/***
	< AJAX REQUEST >
	***/
	var httpRequest1;
	if (window.XMLHttpRequest)
	{ // Mozilla, Safari, ...
		httpRequest1 = new XMLHttpRequest();
		if (httpRequest1.overrideMimeType)
		{
			httpRequest1.overrideMimeType('text/xml');
			// See note below about this line
		}
	} 
	else if (window.ActiveXObject)
	{ // IE
		try
		{
			httpRequest1 = new ActiveXObject("Msxml2.XMLHTTP");
		} 
		catch (e)
		{
			try
			{
				httpRequest1 = new ActiveXObject("Microsoft.XMLHTTP");
			} 
			catch (e) {}
		}
	}

	if (!httpRequest1) {
		alert('Giving up :( Cannot create an XMLHTTP instance');
	}
	httpRequest1.onreadystatechange = function()
	{ 
		if (httpRequest1.readyState == 4) {
				if (httpRequest1.status == 200) {
				} else {
					alert('There was a problem with the request.');
				}
			}
	};
	// Send result to database
	httpRequest1.open('POST', "result.php", true);
	httpRequest1.send(data);
	/***
	</ Ajax Request >
	***/

	qiter++;
	if (qiter >= questions.length-2) {
		finish();
		return true;
	}
	// Increment the question
	document.getElementById("question").innerHTML = "Question ".concat(qiter+1, ": ", questions[qiter][0]);
	document.getElementById("Astate").innerHTML = questions[qiter][1];
	document.getElementById("Bstate").innerHTML = questions[qiter][2];
	document.getElementById("Cstate").innerHTML = questions[qiter][3];
	document.getElementById("Dstate").innerHTML = questions[qiter][4];
}

function check()
{
	// Verify a response has been checked
	var chx = document.getElementsByTagName('input');
	var checked = false;
	for (var i=0; i<chx.length; i++) {
		if (chx[i].type == 'radio' && chx[i].checked) {
			checked = true;
		} 
	}
	if (!checked) {
		return false;
	}
	else {
		next();
		return false;
	}
}
</script>
	</head>
	<body>
	<center>
	<h2>Quiz of the Day</h2>
<form name = "quizQuestion" action = "" method = "POST" onSubmit="return check()">
	<p id="title"></p>
	<p id="question"></p>
	<div id="div1">
		<input type="radio" name="answer" id="a"> <label for="a" id="Astate"></label> <br>
		<input type="radio" name="answer" id="b"> <label for="b" id="Bstate"></label> <br>
		<input type="radio" name="answer" id="c"> <label for="c" id="Cstate"></label> <br>
		<input type="radio" name="answer" id="d"> <label for="d" id="Dstate"></label> <br>
		<input id = "sub" type="submit" name="submit" value="submit">
	<p id="finish"></p>
	<p id="overall"></p>
	</div>
</form>
	</center>
	</body>
</html>
