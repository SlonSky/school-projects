<?php

class Router {

	private $route;
	private $defaultController = 'PagesController';

	public function __construct($path) {
		$this->route = explode('/', $path);

	}

	public function getController() {
		$controller = $this->getControllerName();
		$action = $this->getAction();
		if(class_exists($controller)) {	
			return new $controller($action);
		} else {
			throw new Exception("Error 404: Controller not found - " . $controller, 404); // Page not found
		}
	}

	private function getControllerName() {
		if(empty($this->route) || empty($this->route[0])) {
			return $this->defaultController;
		}
		$name = array_shift($this->route);
		if(!preg_match('#^[a-zA-Z0-9.,-]*$#', $name)) {
			throw new Exception("Error 400: Invalid path", 400); // Bad request
		} 
		return ucfirst($name) . 'Controller';
	}

	private function getAction() {
		$name = array_shift($this->route);
		if(empty($name)) {
			return null;
		}
		if(!preg_match('#^[a-zA-Z0-9.,-]*$#', $name)) {
			throw new Exception("Error 400: Invalid path", 400);
		} 
		return $name;
	}
}