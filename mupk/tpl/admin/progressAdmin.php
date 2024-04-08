<section>
    <div class="mainImage"><img class="main" src="images/progres.jpg"></div>
    <h1>Успішність учнів</h1>
    <h3><a style="margin-left: 20%" href="?Admin/addStudentForm">Додати учня</a></h3>
    <div  class="progress">
        <h3>Введіть дані для пошуку групи:</h3>
        <form method="post" action="?progress">
            <select name="school" >
                <option value="БЗШ № 3">БЗШ № 3</option>
                <option value="КринОШ">КринОШ</option>
                <option value="ОксОШ">ОксОШ</option>
            </select>
            <select name="specialty">
                <option value="Operator">Оператор</option>
                <option value="Secretary">Секретар</option>
                <option value="Driver B">Водій B</option>
            </select>
            <select name="day">
                <option value="Monday">Понеділок</option>
                <option value="Tuesday">Вівтрок</option>
                <option value="Wednesday">Середа</option>
                <option value="Thursday">Четвер</option>
                <option value="Friday">П'ятниця</option>
            </select>
            <select name="class">
                <option value="10">10 клас</option>
                <option value="11">11 клас</option>
            </select>
            <input type="submit" value="Шукати">
        </form></div>

    <?php
    echo "<div class='mes'>";
    if(count($this->students) < 1) {
        echo "<div>Не знайдено записів.</div>";
    } else {
        echo "<h4>Результати пошуку:</h4><table><tr><td><b>Учень</b></td><td><b>Школа</b></td></tr>";
        foreach($this->students as $student){
            echo "<tr><td>".$student["name"]."</td><td>".$student["school"]."</td><td><a href='?Admin/deleteStudent/".$student["id"]."'> Видалити</a></td></tr>";
        }
        echo "</table></div>";
    }
    ?>
</section>
<div class="separator"></div>

