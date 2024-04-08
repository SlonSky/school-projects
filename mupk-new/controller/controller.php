<?php

class Controller {

	protected $action = 'index';
	protected $name;
	protected $content;

	public function __construct($action = null) {
		// create database, e.g.:
		// $dataBase = new DataBase('index');

		$className = str_replace('Controller', '', get_class($this));
		$splitted = explode('\\', $className);
		$className = $splitted[count($splitted) - 1];
		$this->name = strtolower($className);

		if($action !== null) {
			$this->action = $action;
		}

		$methodName = 'action'.ucfirst($this->action);
		if(method_exists($this, $methodName)) {
			$this->$methodName();
		} else {
			throw new Exception("Error 404: Method not found - " . $methodName, 404);
		}
	}


	public function render($header = null, $footer = null) {
		ob_start(); 
		{
			if($header !== null) {
				include_once($header);
			}
			include_once('/views/' . $this->name . '/' . $this->action . '.php');
			if($footer !== null) {
				include_once($footer);
			}
			$this->content = ob_get_contents();
		}
		ob_end_clean();
	}

	public function content() {
		return $this->content;
	}
}