<?php

class ctrl{
    public function __construct(){
        $this->db = new db();
    }

    public function out($tplName, $nested=false){
        if(!$nested){
            $this->tpl = $tplName;
            include "tpl/main.php";
        } else {
            include "tpl/".$tplName;
        }
    }
}

class app{
    public function __construct($path){
        $this->route = explode("/", $path);
        $this->run();
    }

    private function run(){
        $url = array_shift($this->route);
        if(!preg_match("#^[a-zA-Z0-9.,-]*$#", $url)) throw new Exception('Invalid path');
        $ctrlName = 'ctrl'. ucfirst($url);
        if(file_exists('app/'.$ctrlName.".php")){
            $this->runController($ctrlName);
        } else {
            array_unshift($this->route, $url);
            $this->runController('ctrlIndex');
        }
    }

    private function runController($ctrlName){
        include "app/".$ctrlName.".php";
        $ctrl = new $ctrlName();
        if(empty($this->route) || empty($this->route[0])){
            $ctrl->index();
        } else {
            if(empty($this->route)) {
                $method = 'index';
            }
            else {
                $method = array_shift($this->route);
            }
            if(count($this->route) > 0){
                $this->callMethod($ctrl, $method, array_shift($this->route));
            } else {
                $this->callMethod($ctrl, $method);
            }

        }
    }

    private function callMethod($ctrl, $method, $arg=null){
        if(method_exists($ctrl, $method)){
            $ctrl->$method($arg);
        } else throw new Exception("Error 404");
    }
}