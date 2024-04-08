<section>
    <h1>Додати учня</h1>
    <div  class="progress">
        <h3>Введіть дані:</h3>
        <form style="margin-bottom: 10px" method="post" action="?Admin/addStudent">
            <p>
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
            </select></p>
            <p>
                <label>Ім'я</label><br>
                <input type="text" name="name">
            </p>
            <p>
                <label>Дата нарождення</label><br>
                <input type="date" name="birthday">
            </p>
            <input type="submit" value="Додати">
        </form></div>
</section>
<div class="separator"></div>