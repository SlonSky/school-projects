<!-- popup menu -->
<div id="parentPopup" onclick="hideOnOutClick()">
    <div id="popup" onclick="setPopupFocus(true)">
        <img src="images/close.png" id="close" onclick="hidePopup()">

        <!-- login form -->
        <form id="loginForm" class="innerForm" action="?Login/testReg" method="post" onsubmit="checkLoginData(); return false;">
            <h3>Вхід</h3>
            <p><label>Ваш логін:<br></label>
                <input name="login" id="login" type="text" size="15" maxlength="15"></p>
            <p><label>Ваш пароль:<br></label>
                <input name="password" id="password" type="password" size="15" maxlength="15"></p>
            <p><input type="submit" name="submit" value="Увійти"><br></p>
            <p class="message" id="message"></p>
        </form>

        <!-- registration form -->
        <form id="registerForm" class="innerForm" action="?Login/save" method="post" onsubmit="checkRegisterData(); return false;">
            <h3>Реєстрація</h3>
            <p><label>Ваш логін:<br></label>
                <input name="login" id="loginReg" type="text" size="15" maxlength="15"></p>
            <p><label>Ваш пароль:<br></label>
                <input name="password" id="passwordReg" type="password" size="15" maxlength="15"></p>
            <p><input type="submit" name="submit" value="Зареєструватися"></p>
            <p class="message" id="messageReg"></p>
        </form>
    </div>
</div>

<script>

    var popupInFocus = false;
    var validLogin = new RegExp("[a-zA-Z0-9а-яА-Я_]");

    function checkLoginData(){
        if(document.getElementById("login").value.toString() == "" || document.getElementById("password").value.toString() == ""){
            document.getElementById("message").innerHTML = "Будь ласка, введіть логін і пароль";
        } else {
            this.submit();
        }
    }

    function checkRegisterData(){
        if(document.getElementById("loginReg").value.toString() == "" || document.getElementById("passwordReg").value.toString() == ""){
            document.getElementById("messageReg").innerHTML = "Будь ласка, введіть логін і пароль";
        } else if(!validLogin.test((document.getElementById("loginReg").value.toString()))){
            document.getElementById("messageReg").innerHTML = "Невірний формат логіну";
        } else if(document.getElementById("passwordReg").value.toString().length <  6){
            document.getElementById("messageReg").innerHTML = "Мінімальна довжина паролю - 6 символів";
        } else {
            this.submit();
        }
    }

    function hideOnOutClick(){
        if(popupInFocus == false){
            hidePopup();
        }
        setPopupFocus(false);
    }

    function setPopupFocus(focus){ popupInFocus = focus; }

    function hidePopup(){
        document.getElementById("parentPopup").style.display="none";
        document.getElementById("loginForm").style.display="none";
        document.getElementById("registerForm").style.display="none";
    }

    function showLogin(){
        document.getElementById("parentPopup").style.display="block";
        document.getElementById("loginForm").style.display="block";
    }

    function showRegister(){
        document.getElementById("parentPopup").style.display="block";
        document.getElementById("registerForm").style.display="block";
    }

</script>