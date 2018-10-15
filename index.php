<html>
<head>
	<title>Blondeman's PythPage</title>
</head>

<?php
session_start();
$_SESSION['pagename']="python index";

	error_reporting(0);
	if ($handle = opendir('.')) {
	while (false !== ($file = readdir ($handle)))
	{
		if ($file != "." && $file != ".." && $file != "index.php" && $file
		!= "find-factors.png" && $file != "multiplication.png" && $file != "quadratic.png"
		&& $file != "README.md" && $file != ".git" && $file != "htaccess.png")
		{
			$thelist .= '<li><a href="'.$file.'"class = "bttn bttn2" target = "_blank">'.$file.'</a></li>';
		}
		
	}
	closedir($handle);
}
?>

<body>
<p>Files:</p>
<ul>
<?php echo $thelist?>
</ul>
</div>
</body>
</html>
