<?php

class db{

    public function __construct(){
//        $this->mysqli = new mysqli("localhost", "Slonsky", "slonsky", "UPK"); // localhost
        $this->mysqli = new mysqli("mysql.hostinger.pl", "u339875547_mupk", "mupkbolgrad9999", "u339875547_mupk"); // server
    }

    public function query($sql){

        $args = func_get_args();

        $sql = array_shift($args);
        $link = $this->mysqli;
        $args = array_map(function ($param) use ($link){
            return $link->escape_string($param);
        }, $args);

        $sql = str_replace(array('%', '?'), array('%%', '%s'), $sql);

        array_unshift($args, $sql);

        call_user_func_array('sprintf', $args);

        $this->last = $this->mysqli->query($sql);
        if($this->last === false) throw new Exception("Database error: ".$this->mysqli->error);
        return $this;
    }

    public function assoc(){
        return $this->last->fetch_assoc();
    }

    public function all(){
        $result = array();
        while($row = $this->last->fetch_array())
            $result[] = $row;
        return $result;
    }
}