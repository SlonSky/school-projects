<!DOCTYPE html >
<html lang="ua">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/main.css">
    <link rel="icon" href="images/logo.jpg">
    <title>Болградьский МНВК</title>
</head>

<body onload="hidePopup()">
<header id="pageHeader">
    <a href="?" id="titleImage"><img src="images/logo.jpg"></a>
    <nav>
        <ul>
            <li><a href="">Все про нас</a>
                <ul class="sub">
                    <li><a href="?team">Педколектив</a></li>
                    <li><a href="?career">Профорієнтаційна робота</a></li>
                    <li><a href="?education">Профільне навчання</a></li>
                    <li><a href="?regulatory">Нормативно-правова база</a></li>
                    <li><a href="?validation">Атестація педпрацівників</a></li>
                </ul>
            </li>
            <li><a href="">Наші учні</a>
                <ul class="sub">
                    <li><a href="?progress">Успішність учнів</a></li>
                    <li><a href="?graduates">Випуск учнів</a></li>
                </ul>
            </li>
            <li><a href="?gallery">Фотогалерея</a></li>
        </ul>
    </nav>

    <div class="auth">
        <?php
        if (empty($_SESSION['login']) or empty($_SESSION['id'])) {
            echo "<span style='cursor: pointer' onclick='showLogin();'>Увійти</span>|<span style='cursor: pointer'  onclick='showRegister()'>Реєстрація</sp>";
        } else {
            echo "<a href=\"\" class='clear'>".$_SESSION['login']."</a>
              <a href=\"?Login/userExit\" class='clear'>Вийти</a>";
        }
        ?>
    </div>
</header>

<?php include("tpl/regForms.php"); ?>

<section>
<?php $this->out($this->tpl, true); ?>
</section>

<footer id="pageFooter">
    <div>2016 | <b>Болградський міжшкільний навчально-виробничий комбінат</b><br></div>
    <div>адреса: 68702, Україна, Одеська область,
        м.Болград, пр.Леніна, 154
        <br></div>
    <div>тел./факс: (804846) 4-28-95</div>
</footer>
</body>
</html>


