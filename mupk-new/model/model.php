<?php
class Model {
	protected $dataBase;

	public function __construct($dataBase) {
		$this->dataBase = new mysqli(
			$dataBase['server'], 
			$dataBase['user'], 
			$dataBase['password'], 
			$dataBase['dbName']);

		if(mysqli_connect_errno()) {
			throw new Exception("Database error: " . mysqli_connect_error(), 1);
		}
	}

	protected function query($query) {
		$result = $this->dataBase->query($query);
		// todo: close result?
		return $result;
	}

	public function __destruct() {
		$dataBase->close();
	}
}