<?php

require_once('./controller/router.php');
require_once('./controller/controller.php');
require_once('./controller/pages_controller.php');

require_once('./config/databases.php');

require_once('./model/pages_model.php');

$router = new Router(substr($_SERVER['REQUEST_URI'], 1));

// todo: catch exceptions
$controller = $router->getController();
echo $controller->content();	

// try {
// 	$controller = $router->getController();
// 	echo $controller->content();	
// } 
// catch (Exception $e) {
// 	switch ($e->getCode()) {
// 		case 404:
// 			echo "<h1>Page not found</h1><p>".$e->getMessage()."</p>";
// 			break;
// 		case 400:
// 			echo "<h1>Bad request</h1><p>".$e->getMessage()."</p>";
// 			break;
// 		default:
// 			# code...
// 			break;
// 	}
	// echo "<p>".print_r($e->getTrace())."</p>";
// }





// try {
// 	$controller = new PagesController();	
// 	echo $controller->content();
// } catch(Exception $e) {
// 	if($e->getCode() == 404) {
// 		echo "<h1>Page not found</h1>";
// 	}
// }











 // <?
	// $db = mysqli_connect(
	// 	'localhost', 
	// 	'root', 
	// 	'admin', 
	// 	'Forum');

	// $res = mysqli_query($db, 'SHOW TABLES');
	// while ($row = mysqli_fetch_assoc($res)) {
	// 	echo $row['Tables_in_forum'];
	// 	print("\n");

	// }

	// mysqli_free_result($res);
	// mysqli_close($db);

// $mysqli = new mysqli('localhost', 'root', 'admin', 'Forum');
// if(mysqli_connect_errno()) {
// 	print("MySQL error ocured: " . mysqli_connect_errror());
// 	exit;
// }

// if($res = $mysqli->query("SHOW TABLES")) {
// 	while ($row = $res->fetch_assoc()) {
// 		echo $row['Tables_in_forum'];
// 		print("\n");
// 	}

// 	$res->close();
// }

// $mysqli->close();

// 