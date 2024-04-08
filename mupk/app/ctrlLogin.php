<?php
class ctrlLogin extends ctrl{

    function testReg(){
        session_start();

        if (isset($_POST['login'])) { $login = $_POST['login']; if ($login == '') { unset($login);} }
        if (isset($_POST['password'])) { $password=$_POST['password']; if ($password =='') { unset($password);} }

        $login = stripslashes($login);
        $login = htmlspecialchars($login);
        $password = stripslashes($password);
        $password = htmlspecialchars($password);

        $login = trim($login);
        $password = trim($password);

        $myrow = $this->db->query("SELECT * FROM users WHERE login='$login'")->assoc();

        if (empty($myrow['password'])) {
            exit("<!DOCTYPE html><html lang='ua'><head><meta charset='utf-8'><meta    http-equiv='Refresh' content='1; URL=http://mupk.hol.es/'></head><body>
          <h1 style='text-align: center'>Помилка авторизації</h1></body></html>");
        } else {
            if ($myrow['password']==$password) {
                $_SESSION['login']=$myrow['login'];
                $_SESSION['id']=$myrow['id'];
                exit("<!DOCTYPE html><html lang='ua'><head><meta charset='utf-8'><meta http-equiv='Refresh' content='0; URL=http://mupk.hol.es/'></head><body></body></html>");
            } else {
                exit("<!DOCTYPE html><html lang='ua'><head><meta charset='utf-8'><meta    http-equiv='Refresh' content='1; URL=http://mupk.hol.es/'></head><body>
          <h1 style='text-align: center'>Помилка авторизації</h1></body></html>");
            }
        }
    }

    function userExit(){
        session_start();

        // destroy session
        unset($_SESSION['password']);
        unset($_SESSION['login']);
        unset($_SESSION['id']);

        // back to index
        exit("<!DOCTYPE html><html lang='ua'><head><meta charset='utf-8'><meta    http-equiv='Refresh' content='0;    URL=http://mupk.hol.es/'></head><body></body></html>");

    }


    function save(){

        // field data checking
        if (isset($_POST['login'])) { $login = $_POST['login']; if ($login == '') { unset($login);} }
        if (isset($_POST['password'])) { $password=$_POST['password']; if ($password =='') { unset($password);} }

        // delete tags
        $login = stripslashes($login);
        $login = htmlspecialchars($login);
        $password = stripslashes($password);
        $password = htmlspecialchars($password);

        // trim whitespaces
        $login = trim($login);
        $password = trim($password);

        // existing user checking
        $existingID =  $this->db->query("SELECT id FROM users WHERE login='$login'")->all();
        echo $existingID['id'];
        if (!empty($existingID['id'])) {
            exit("<!DOCTYPE html><html lang='ua'><head><meta charset='utf-8'><meta    http-equiv='Refresh' content='1; URL=http://mupk.hol.es/'></head><body>
                    <h1 style='text-align: center'>Помилка реєстрації - логін існує</h1>
                       </body></html>");
        }

        // insert user to DB
        try{
            $this->db->query("INSERT INTO users (login,password) VALUES('$login','$password')");
        } catch (Exception $e){
            exit("<!DOCTYPE html><html lang='ua'><head><meta charset='utf-8'><meta    http-equiv='Refresh' content='1; URL=http://mupk.hol.es/'></head><body>
                    <h1 style='text-align: center'>Помилка реєстрації</h1>
                       </body></html>");
        }

        // to index
        exit("<!DOCTYPE html><html lang='ua'><head><meta charset='utf-8'><meta    http-equiv='Refresh' content='0;    URL=http://mupk.hol.es/'></head><body></body></html>");
    }
}