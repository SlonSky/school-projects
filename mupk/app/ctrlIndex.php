<?php

class ctrlIndex extends ctrl{

    function index(){

        include ("ctrlAdmin.php");
        $this->admin = new ctrlAdmin();

        if($this->admin->isAdmin()){
            $this->admin->index();
        } else {
            $this->posts = $this->db->query("SELECT * FROM posts ORDER BY ctime DESC")->all();
            $this->out("news.php");
        }
    }

    function team(){
        $this->out("team.html");
    }

    function career(){
        $this->out("career.php");
    }

    function progress(){
        $school = $_POST["school"];
        $specialty = $_POST["specialty"];
        $day = $_POST["day"];
        $class = $_POST["class"];
        $this->students = $this->db->query("SELECT * FROM students WHERE (school, specialty, day, class)=('$school', '$specialty', '$day', '$class')")->all();


        include ("ctrlAdmin.php");
        $this->admin = new ctrlAdmin();
        if($this->admin->isAdmin()){
            $this->admin->progress($this->students);
        } else {
            $this->out("progress.php");
        }
    }

    function education(){
        $this->out("education.html");
    }

    function regulatory(){
        $this->out("regulatory.html");
    }

    function validation(){
        $this->out("validation.html");
    }

    function graduates(){
        $this->out("graduates.php", true);
    }

    function gallery(){
        $this->out("gallery.php", true);
    }
}