<?php

$_PAGES = [
	'main' => 1,
	'career' => 2,
	'education' => 3,
	'progress' => 4,
	'regulatory' => 5,
	'validation' => 6,
	'team' => 7
];

class Page {

	private $header;
	private $content;
	private $imageLink;

	public function __construct($header, $content, $imageLink) {
		$this->header = $header;
		$this->content = $content;
		$this->imageLink = $imageLink;
	}

	public function header() {
		return $this->header;
	}

	public function content() {
		return $this->content;
	}

	public function imageLink() {
		return $this->imageLink;
	}
}

class PagesModel extends Model {

	public function getPage($headerID) {
		$result = query('SELECT * FROM pages WHERE id = ' . $headerID . ';');
		$result = $result->fetch_assoc();
		$page = new Page($result['header'], $result['content'], $result['imageLink']);
	}	
}