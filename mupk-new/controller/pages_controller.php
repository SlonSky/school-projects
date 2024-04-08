<?php

class PagesController extends Controller{

	private $header = './views/pages/mainHeader.php';
	private $footer = './views/pages/mainFooter.php';

	private $database;
	private $page;


	public function __construct($action = null) {
		parent::__construct($action);

		$this->database = new PagesDatabase($_DATABASES['views']);
	}

	public function actionIndex() {
		$this->page = $this->database->getPage($_PAGES['main']);
		$this->render($this->header, $this->footer);
	}

	// temp
	public function actionCareer() {
		$this->page = $this->database->getPage($_PAGES['career']);
		$this->render($this->header, $this->footer);	
	}

}